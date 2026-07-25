from models.video import Video
from models.video_result import VideoResult


class VideoFactory:

    @staticmethod
    def from_result(result: VideoResult, produto_id: int):

        video = Video()

        video.produto_id = produto_id

        video.video_id = result.video_id
        video.titulo = result.titulo
        video.url = result.url
        video.thumbnail = result.thumbnail
        video.canal = result.canal

        video.views = result.views
        video.likes = result.likes
        video.duracao = result.duracao

        video.score = result.score
        video.provider = result.provider

        return video

    # -------------------------------------------------------
    # Compatibilidade com código legado
    # -------------------------------------------------------

    @staticmethod
    def from_dict(data, produto_id):

        if isinstance(data, VideoResult):
            return VideoFactory.from_result(data, produto_id)

        video = Video()

        video.produto_id = produto_id

        video.video_id = data.get("video_id")
        video.titulo = data.get("titulo")
        video.url = data.get("url")
        video.thumbnail = data.get("thumbnail")
        video.canal = data.get("canal")

        video.views = data.get("views", 0)
        video.likes = data.get("likes", 0)
        video.duracao = data.get("duracao", 0)

        video.score = data.get("score", 0)
        video.provider = data.get("provider", "")

        return video