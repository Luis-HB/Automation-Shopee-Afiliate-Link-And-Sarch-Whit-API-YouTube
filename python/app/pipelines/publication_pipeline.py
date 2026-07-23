from services.status.status_service import StatusService
from services.publication.published_video_selector import PublishedvideoSelector


class PublicationPipeline:

    def __init__(self):

        self.selector = PublishedvideoSelector()

    def process(self, product):

        if product.status != StatusService.PRONTO:

            raise Exception(
                f"Produto não está pronto para publicação ({product.status})"
            )

        video = self.selector.select(product)

        if not video:

            raise Exception(
                "Produto não possui vídeos."
            )

        print(f"Publicando {product.titulo}")
        print(f"Vídeo escolhido: {video.titulo}")

        StatusService.publicado(product)

        return video