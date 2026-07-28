import time

from services.video.video_discovery_service import VideoDiscoveryService
from services.search.search_query_service import SearchQueryService
from services.status.status_service import StatusService


class DiscoverVideosAction:

    def __init__(self):

        self.discovery = VideoDiscoveryService()
        self.search_queries = SearchQueryService()

    # =====================================================
    # Execução
    # =====================================================

    def execute(
        self,
        product,
        queries,
        result
    ):

        print("3 - Discovery")

        StatusService.buscando_videos(product)

        started = time.perf_counter()

        # -------------------------------------------------
        # Registra todas as consultas como PENDING
        # -------------------------------------------------

        registros = {}

        consultas = []

        for item in queries:

            registro = self.search_queries.start(

                produto_id=product.id,

                provider=item["provider"],

                query=item["query"],

                ordem=item["ordem"]

            )

            chave = (
                item["provider"],
                item["query"],
                item["ordem"]
            )

            registros[chave] = registro

            consultas.append(item)

        # -------------------------------------------------
        # Descoberta
        # -------------------------------------------------

        try:

            discovery = self.discovery.search(consultas)

        except RuntimeError:

            raise

        except Exception as e:

            print(e)

            for registro in registros.values():

                self.search_queries.fail(registro)

            StatusService.erro(product)

            return None

        # -------------------------------------------------
        # Atualiza status das consultas
        # -------------------------------------------------

        for query_result in discovery.queries:

            chave = (

                query_result.provider,

                query_result.query,

                query_result.ordem

            )

            registro = registros.get(chave)

            if registro is None:
                continue

            elapsed_ms = int(query_result.elapsed * 1000)

            if query_result.total > 0:

                self.search_queries.success(

                    registro,

                    videos_found=query_result.total,

                    elapsed_ms=elapsed_ms

                )

            else:

                self.search_queries.empty(

                    registro,

                    elapsed_ms=elapsed_ms

                )

        # -------------------------------------------------
        # Metadata
        # -------------------------------------------------

        elapsed = round(

            time.perf_counter() - started,

            2

        )

        result.discovery = discovery

        result.set_metadata(

            videos_found=discovery.total,

            queries_processed=discovery.queries_total,

            providers=discovery.providers,

            failed_providers=discovery.failed_providers,

            discovery_time=elapsed

        )

        # -------------------------------------------------
        # Nenhum vídeo
        # -------------------------------------------------

        if discovery.total == 0:

            print("Nenhum vídeo encontrado.")

            StatusService.sem_video(product)

            return None

        print(f"Vídeos encontrados: {discovery.total}")

        return discovery

    # =====================================================
    # Alias
    # =====================================================

    def executar(self, *args, **kwargs):

        return self.execute(*args, **kwargs)