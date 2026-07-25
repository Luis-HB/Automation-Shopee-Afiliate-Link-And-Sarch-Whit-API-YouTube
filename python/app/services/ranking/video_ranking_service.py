import time

from models.ranking_result import RankingResult
from services.ranking.score_service import ScoreService


class VideoRankingService:

    @staticmethod
    def rank(produto, videos, limite=10, limit=None):

        start = time.perf_counter()

        if limit is not None:
            limite = limit

        resultado = RankingResult()

        unicos = {}

        # Remove duplicados
        for video in videos:

            if video.video_id not in unicos:

                unicos[video.video_id] = video

        # Calcula score

        for video in unicos.values():

            video.score = ScoreService.calculate(
                produto,
                video
            )

        ordenados = sorted(

            unicos.values(),

            key=lambda x: x.score,

            reverse=True

        )

        aprovados = ordenados[:limite]

        resultado.videos = aprovados

        resultado.discarded = max(
            0,
            len(ordenados) - len(aprovados)
        )

        resultado.elapsed = round(

            time.perf_counter() - start,

            3

        )

        resultado.calculate_statistics()

        return resultado

    # ---------------------------------------------------
    # Compatibilidade
    # ---------------------------------------------------

    @staticmethod
    def rankear(produto, videos, limite=10):

        return VideoRankingService.rank(
            produto,
            videos,
            limite
        )