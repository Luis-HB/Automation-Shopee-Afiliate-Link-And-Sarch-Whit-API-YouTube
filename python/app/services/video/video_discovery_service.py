import time

from models.discovery_result import DiscoveryResult
from models.query_result import QueryResult

from services.video.provider_loader import ProviderLoader
from services.video.provider_registry import ProviderRegistry
from services.video.provider_executor import ProviderExecutor


class VideoDiscoveryService:

    def __init__(self):

        ProviderLoader.load()

        self.providers = ProviderRegistry.providers()

    # =====================================================
    # Descoberta
    # =====================================================

    def buscar(self, consultas):

        inicio = time.perf_counter()

        resultado = DiscoveryResult()

        videos_unicos = {}

        for consulta in consultas:

            provider_name = consulta["provider"]
            query = consulta["query"]
            ordem = consulta["ordem"]

            query_result = QueryResult(

                provider=provider_name,

                query=query,

                ordem=ordem

            )

            provider = self._find_provider(provider_name)

            if provider is None:

                resultado.add_failed_provider(provider_name)

                resultado.add_query(query_result)

                continue

            try:

                inicio_query = time.perf_counter()

                encontrados = ProviderExecutor.execute(

                    provider,

                    [query]

                )

                query_result.elapsed = round(

                    time.perf_counter() - inicio_query,

                    2

                )

                resultado.add_provider(provider.name)

                for video in encontrados:

                    query_result.videos.append(video)

                    videos_unicos[video.video_id] = video

                resultado.add_query(query_result)

            except RuntimeError as e:

                if str(e) == "YOUTUBE_QUOTA_EXCEEDED":

                    resultado.quota_exceeded = True

                    raise

                resultado.add_failed_provider(provider.name)

                resultado.add_query(query_result)

            except Exception:

                resultado.add_failed_provider(provider.name)

                resultado.add_query(query_result)

        resultado.extend(videos_unicos.values())

        resultado.elapsed = round(

            time.perf_counter() - inicio,

            2

        )

        return resultado

    # =====================================================
    # Auxiliares
    # =====================================================

    def _find_provider(self, provider_name):

        for provider in self.providers:

            if provider.name == provider_name:

                return provider

        return None

    # =====================================================
    # API pública
    # =====================================================

    def search(self, queries):

        return self.buscar(queries)

    def providers_names(self):

        return [

            provider.name

            for provider in self.providers

        ]

    def provider_names(self):

        return self.providers_names()