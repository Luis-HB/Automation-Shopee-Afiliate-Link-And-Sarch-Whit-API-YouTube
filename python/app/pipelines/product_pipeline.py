import time

from models.pipeline_result import PipelineResult

from services.product.product_analyzer import ProductAnalyzer
from services.search.search_query_builder import SearchQueryBuilder
from services.video.video_discovery_service import VideoDiscoveryService
from services.ranking.video_ranking_service import VideoRankingService
from services.status.status_service import StatusService

from repositories.video_repository import VideoRepository
from factories.video_factory import VideoFactory


class ProductPipeline:

    def __init__(self):

        self.analyzer = ProductAnalyzer()
        self.discovery = VideoDiscoveryService()
        self.ranking = VideoRankingService()
        self.video_repo = VideoRepository()

    def process(self, product):

        print("=" * 70)
        print(">>> PRODUCT PIPELINE <<<")
        print(product.titulo)
        print("=" * 70)

        start = time.perf_counter()

        # -------------------------------------------------
        # Produto em processamento
        # -------------------------------------------------

        StatusService.processando(product)

        print("1 - Analyzer")

        self.analyzer.analyze(product)

        result = PipelineResult(product)

        # -------------------------------------------------
        # Geração das consultas
        # -------------------------------------------------

        print("2 - Queries")

        queries = SearchQueryBuilder.generate(product)

        print(queries)

        result.set_metadata(
            source="affiliate_api",
            queries_generated=len(queries),
            search_strategy="multi_provider",
            queries=queries
        )

        # -------------------------------------------------
        # Busca dos vídeos
        # -------------------------------------------------

        print("3 - Descoberta")

        StatusService.buscando_videos(product)

        try:

            discovery = self.discovery.search(queries)

            videos = discovery.videos

            print(f"Vídeos encontrados: {discovery.total}")

        except RuntimeError as e:

            if str(e) == "YOUTUBE_QUOTA_EXCEEDED":

                print()
                print("=" * 70)
                print("QUOTA DA API DO YOUTUBE ESGOTADA")
                print("Interrompendo descoberta de vídeos.")
                print("=" * 70)
                print()

                raise

            raise

        except Exception as e:

            print("ERRO NA BUSCA")
            print(e)

            StatusService.erro(product)

            result.add_error(e)

            result.set_metadata(
                video_error=str(e),
                videos_found=0,
                videos_ranked=0,
                videos_saved=0
            )

            return result.to_dict()

        result.discovery = discovery

        # Compatibilidade temporária
        result.set_metadata(
            videos_found=discovery.total,
            providers=discovery.providers,
            failed_providers=discovery.failed_providers,
            discovery_time=discovery.elapsed
        )

        if discovery.total == 0:

            print("Nenhum vídeo encontrado.")

            StatusService.sem_video(product)

            return result.to_dict()

        # -------------------------------------------------
        # Ranking
        # -------------------------------------------------

        print("4 - Ranking")

        ranking = self.ranking.rank(
            product,
            videos,
            limit=10
        )

        print(f"Ranking gerado: {ranking.total}")

        result.ranking = ranking

        # Compatibilidade temporária
        result.set_metadata(
            videos_ranked=ranking.total,
            average_score=ranking.average_score,
            highest_score=ranking.highest_score,
            lowest_score=ranking.lowest_score,
            ranking_time=ranking.elapsed,
            discarded=ranking.discarded
        )

        if ranking.total == 0:

            print("Nenhum vídeo aprovado no ranking.")

            StatusService.sem_video(product)

            return result.to_dict()

        StatusService.videos_encontrados(product)
        StatusService.ranqueado(product)

        # -------------------------------------------------
        # Persistência
        # -------------------------------------------------

        print("5 - Salvando vídeos")

        videos_saved = 0

        for data in ranking.videos:

            try:

                print(f"Salvando: {data.titulo}")

                video = VideoFactory.from_result(
                    data,
                    product.id
                )

                self.video_repo.upsert(video)

                result.add_video(video)

                videos_saved += 1

            except Exception as e:

                print("Erro ao salvar vídeo:")
                print(e)

                result.add_error(e)

                StatusService.erro(product)

        print(f"Vídeos salvos: {videos_saved}")

        # -------------------------------------------------
        # Status final
        # -------------------------------------------------

        if videos_saved > 0:

            StatusService.pronto(product)
            result.success = True

        else:

            StatusService.sem_video(product)
            result.success = False

        elapsed = round(
            time.perf_counter() - start,
            2
        )

        result.processing_time = elapsed
        result.pipeline = "affiliate"
        result.version = "4.0"

        # Compatibilidade temporária
        result.set_metadata(
            processing_time=elapsed,
            pipeline="affiliate",
            version="4.0",
            videos_saved=videos_saved
        )

        print(f"STATUS FINAL: {product.status}")
        print("=" * 70)

        return result  

    # -------------------------------------------------
    # Alias
    # -------------------------------------------------

    def processar(self, product):
        return self.process(product)