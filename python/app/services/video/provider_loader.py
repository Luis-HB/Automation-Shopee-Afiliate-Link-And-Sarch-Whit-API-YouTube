from providers.youtube_provider import YoutubeProvider
from providers.shopee_video_provider import ShopeeVideoProvider

from services.video.provider_registry import ProviderRegistry


class ProviderLoader:

    _loaded = False

    @classmethod
    def load(cls):

        if cls._loaded:
            return

        ProviderRegistry.register(
            YoutubeProvider()
        )

        ProviderRegistry.register(
            ShopeeVideoProvider()
        )

        cls._loaded = True