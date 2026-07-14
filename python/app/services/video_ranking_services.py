from services.score_service import ScoreService


class VideoRankingService:

    @staticmethod
    def rank(produto, videos, limite=10):

        unicos = {}

        # Remove vídeos duplicados
        for video in videos:

            video_id = video["video_id"]

            if video_id not in unicos:

                unicos[video_id] = video

        resultado = []

        # Calcula score
        for video in unicos.values():

            score = ScoreService.calcular(produto, video)

            video["score"] = score

            resultado.append(video)

        # Ordena do maior para o menor
        resultado.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return resultado[:limite]