from providers.youtube_provider import YoutubeProvider
from providers.shopee_video_provider import ShopeeVideoProvider


class VideoDiscoveryService:

    def __init__(self):

        self.providers = [
            YoutubeProvider(),
            ShopeeVideoProvider()
        ]

    def buscar(self, consultas):

        videos = {}

        for provider in self.providers:

            encontrados = provider.buscar(consultas)

            for video in encontrados:

                videos[video["video_id"]] = video

        return list(videos.values())

    def providers_names(self):

        return [
            provider.__class__.__name__
            for provider in self.providers
        ]