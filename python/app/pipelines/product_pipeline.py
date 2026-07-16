import time

from services.product_analyzer import ProductAnalyzer
from services.search_query_builder import SearchQueryBuilder
from services.video_discovery_service import VideoDiscoveryService
from services.video_ranking_service import VideoRankingService

from repositories.video_repository import VideoRepository

from factories.video_factory import VideoFactory

from services.contexto_produto_builder import ContextoProdutoBuilder


class ProductPipeline:

    def __init__(self):

        self.analyzer = ProductAnalyzer()

        self.discovery = VideoDiscoveryService()

        self.ranking = VideoRankingService()

        self.video_repo = VideoRepository()

    def processar(self, produto):

        inicio = time.perf_counter()

        # -------------------------------------
        # Análise do produto
        # -------------------------------------

        self.analyzer.analisar(produto)

        contexto = (
            ContextoProdutoBuilder()
            .produto(produto)
        )

        # -------------------------------------
        # Geração das consultas
        # -------------------------------------

        consultas = SearchQueryBuilder.gerar(produto)

        for consulta in consultas:

            contexto.add_consulta(consulta)

        contexto.metadata(

            origem="affiliate_api",

            consultas_geradas=len(consultas),

            estrategia_busca="multi_provider"

        )

        # -------------------------------------
        # Descoberta de vídeos
        # -------------------------------------

        try:

            videos = self.discovery.buscar(
                consultas
            )

        except Exception as e:

            contexto.metadata(

                erro_video=str(e),

                videos_encontrados=0,

                videos_rankeados=0,

                videos_salvos=0

            )

            return contexto.build()

        contexto.metadata(

            videos_encontrados=len(videos),

            provedores=self.discovery.providers_names()

        )

        # -------------------------------------
        # Ranking
        # -------------------------------------

        ranking = []

        if videos:

            ranking = self.ranking.rank(

                produto,

                videos,

                limite=10

            )

        contexto.metadata(

            videos_rankeados=len(ranking)

        )

        # -------------------------------------
        # Persistência
        # -------------------------------------

        videos_salvos = 0

        for dados in ranking:

            try:

                video = VideoFactory.from_dict(

                    dados,

                    produto.id

                )

                self.video_repo.upsert(video)

                contexto.add_video(video)

                videos_salvos += 1

            except Exception as e:

                print(

                    f"Erro ao salvar vídeo: {e}"

                )

        tempo = round(

            time.perf_counter() - inicio,

            2

        )

        contexto.metadata(

            videos_salvos=videos_salvos,

            tempo_processamento=tempo,

            pipeline="affiliate",

            versao="3.0"

        )

        return contexto.build()