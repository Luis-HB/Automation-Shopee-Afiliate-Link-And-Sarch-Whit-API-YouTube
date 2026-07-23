from repositories.video_repository import VideoRepository


class PublishedvideoSelector:

    def __init__(self):

        self.repo = VideoRepository()

    def select(self, product):

        videos = self.repo.find_by_produto(product.id)

        if not videos:
            return None

        videos.sort(
            key=lambda v: v.score,
            reverse=True
        )

        return videos[0]