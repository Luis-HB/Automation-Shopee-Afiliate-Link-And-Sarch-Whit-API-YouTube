from models.video import Video
from services.score_service import ScoreService


class VideoFactory:

    @staticmethod
    def from_dict(dados, produto):

        video = Video(
            produto_id=produto.id,
            youtube_id=dados["video_id"],
            titulo=dados["titulo"],
            canal=dados["canal"],
            thumbnail=dados["thumbnail"],
            url=dados["url"],
            views=dados["views"],
            likes=dados["likes"],
            duracao=dados["duracao"],
            score=dados.get("score", 0)
        )

        # Calcula automaticamente o score
        video.score = ScoreService.calcular(
            video,
            produto
        )

        return video