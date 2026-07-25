import time
from services.video.provider_loader import ProviderLoader
from services.video.provider_registry import ProviderRegistry
from services.video.provider_executor import ProviderExecutor
from models.discovery_result import DiscoveryResult

class VideoDiscoveryService:

    def __init__(self):

        ProviderLoader.load()

        self.providers = ProviderRegistry.providers()

    def buscar(self, consultas):

        inicio = time.perf_counter()

        resultado = DiscoveryResult()

        videos = {}

        for provider in self.providers:

            try:

                encontrados = ProviderExecutor.execute(
                    provider,
                    consultas
                )

                resultado.add_provider(provider.name)

                for video in encontrados:

                    videos[video.video_id] = video

            except RuntimeError as e:

                if str(e) == "YOUTUBE_QUOTA_EXCEEDED":

                    resultado.quota_exceeded = True

                    raise

                resultado.add_failed_provider(provider.name)

            except Exception:

                resultado.add_failed_provider(provider.name)

        resultado.extend(videos.values())

        resultado.elapsed = round(
        time.perf_counter() - inicio,
        2
        )

        return resultado

    def search(self, queries):
        return self.buscar(queries)

    def providers_names(self):

        return [
            provider.name
            for provider in self.providers
        ]

    def provider_names(self):
        return self.providers_names()
    # =====================================================
    # Aliases de compatibilidade
    # =====================================================

    def search(self, queries):
        return self.buscar(queries)

    def provider_names(self):
        return self.providers_names()