from services.ranking.video_ranking_service import VideoRankingService
from services.status.status_service import StatusService


class RankVideosAction:

    def __init__(self):

        self.ranking = VideoRankingService()

    def execute(self, product, discovery, result):

        print("4 - Ranking")

        ranking = self.ranking.rank(

            product,

            discovery.videos,

            limit=10

        )

        print(f"Ranking gerado: {ranking.total}")

        result.ranking = ranking

        result.set_metadata(

            videos_ranked=ranking.total,

            average_score=ranking.average_score,

            highest_score=ranking.highest_score,

            lowest_score=ranking.lowest_score,

            ranking_time=ranking.elapsed,

            discarded=ranking.discarded

        )

        if ranking.total == 0:

            print("Nenhum vídeo aprovado no ranking.")

            StatusService.sem_video(product)

            return None

        StatusService.videos_encontrados(product)

        StatusService.ranqueado(product)

        return ranking

    # ------------------------------------
    # Compatibilidade
    # ------------------------------------

    def process(self, product, discovery, result):
        return self.execute(product, discovery, result)

    def executar(self, product, discovery, result):
        return self.execute(product, discovery, result)