from models.video import Video
from models.video_result import VideoResult


class VideoFactory:

    @staticmethod
    def from_result(result: VideoResult, produto_id: int) -> Video:

        return Video(

            produto_id=produto_id,

            youtube_id=result.video_id,

            titulo=result.titulo,

            canal=result.canal,

            thumbnail=result.thumbnail,

            url=result.url,

            views=result.views,

            likes=result.likes,

            duracao=result.duracao,

            score=result.score

        )

    # -------------------------------------------------------
    # Compatibilidade temporária
    # -------------------------------------------------------

    @staticmethod
    def from_dict(data, produto_id):

        if isinstance(data, VideoResult):
            return VideoFactory.from_result(data, produto_id)

        return Video(

            produto_id=produto_id,

            youtube_id=data.get("video_id", ""),

            titulo=data.get("titulo", ""),

            canal=data.get("canal", ""),

            thumbnail=data.get("thumbnail", ""),

            url=data.get("url", ""),

            views=data.get("views", 0),

            likes=data.get("likes", 0),

            duracao=data.get("duracao", 0),

            score=data.get("score", 0)

        )