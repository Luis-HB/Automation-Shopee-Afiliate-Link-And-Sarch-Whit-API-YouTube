from models.video import Video

from services.ranking.score_service import ScoreService


class VideoFactory:

    @staticmethod
    def from_dict(data, product):

        video = Video(

            produto_id=product.id,

            youtube_id=data["video_id"],

            titulo=data["titulo"],

            canal=data["canal"],

            thumbnail=data["thumbnail"],

            url=data["url"],

            views=data["views"],

            likes=data["likes"],

            duracao=data["duracao"],

            score=data.get("score", 0)

        )

        video.score = ScoreService.calculate(

            video,

            product

        )

        return video