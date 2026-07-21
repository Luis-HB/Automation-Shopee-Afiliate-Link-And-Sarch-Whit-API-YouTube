from services.ranking.score_service import ScoreService


class VideoRankingService:

    @staticmethod
    def rank(produto, videos, limite=10, limit=None):

        # Se 'limit' em inglês for passado, usa ele
        if limit is not None:
            limite = limit

        unicos = {}

        # Remove vídeos duplicados
        for video in videos:

            video_id = video.get("video_id")

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