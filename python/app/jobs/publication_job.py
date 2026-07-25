from repositories.product_repository import ProductRepository

from pipelines.publication_pipeline import PublicationPipeline

from services.publication.publication_payload_builder import (
    PublicationPayloadBuilder
)

from services.publication.webhook_publisher import (
    WebhookPublisher
)

from services.status.status_service import StatusService


class PublicationJob:

    def __init__(self):

        self.products = ProductRepository()

        self.pipeline = PublicationPipeline()

    def execute(self):

        product = self.products.buscar_pronto()

        if not product:

            print("Nenhum produto PRONTO.")

            return

        print(f"Produto: {product.titulo}")

        video = self.pipeline.process(product)

        payload = PublicationPayloadBuilder.build(

            product,

            video

        )

        resposta = WebhookPublisher.publish(

            payload

        )

        StatusService.publicado(product)

        print(resposta)