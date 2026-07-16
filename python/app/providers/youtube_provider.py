from python.app.services.video.youtube_service import YouTubeService

from providers.base_video_provider import BaseVideoProvider


class YoutubeProvider(BaseVideoProvider):

    def __init__(self):

        self.youtube = YouTubeService()

    def buscar(
        self,
        consultas
    ):

        videos = {}

        for consulta in consultas:

            encontrados = self.youtube.buscar_shorts(
                consulta,
                maxResults=10
            )

            for video in encontrados:

                videos[
                    video["video_id"]
                ] = video

        return list(videos.values())