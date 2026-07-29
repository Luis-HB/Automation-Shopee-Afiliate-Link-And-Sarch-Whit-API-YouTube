from repositories.video_repository import VideoRepository
from repositories.search_result_repository import SearchResultRepository

from factories.video_factory import VideoFactory
from factories.search_result_factory import SearchResultFactory

from services.status.status_service import StatusService


class SaveVideosAction:

    def __init__(self):

        self.video_repo = VideoRepository()

        self.search_result_repo = SearchResultRepository()

    # =====================================================

    def execute(self, product, ranking, result):

        print("5 - Salvando vídeos")

        videos_saved = 0

        position = 1

        for video_result in ranking.videos:

            try:

                print(f"Salvando: {video_result.titulo}")

                # ---------------------------------------------
                # Salva o vídeo
                # ---------------------------------------------

                video = VideoFactory.from_result(

                    video_result,

                    product.id

                )

                video = self.video_repo.upsert(video)

                # ---------------------------------------------
                # Histórico da busca
                # ---------------------------------------------

                if video_result.query_id is not None:

                    search_result = SearchResultFactory.create(

                        query_id=video_result.query_id,

                        video=video,

                        position=position,

                        raw_score=video_result.score,

                        ranking_score=video_result.score,

                        selected=True,

                    )

                    self.search_result_repo.save(

                        search_result

                    )

                result.add_video(video)

                videos_saved += 1

                position += 1

            except Exception as e:

                print("Erro ao salvar vídeo:")

                print(e)

                result.add_error(e)

                StatusService.erro(product)

        print(f"Vídeos salvos: {videos_saved}")

        return videos_saved

    # =====================================================

    def process(self, product, ranking, result):

        return self.execute(

            product,

            ranking,

            result

        )

    def executar(self, product, ranking, result):

        return self.execute(

            product,

            ranking,

            result

        )