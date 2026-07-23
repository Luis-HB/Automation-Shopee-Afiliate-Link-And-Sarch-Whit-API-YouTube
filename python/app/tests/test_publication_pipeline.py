from decimal import Decimal
import uuid

from models.product import Product
from models.video import Video

from repositories.product_repository import ProductRepository
from repositories.video_repository import VideoRepository

from pipelines.publication_pipeline import PublicationPipeline

from services.status.status_service import StatusService


product_repo = ProductRepository()
video_repo = VideoRepository()

produto = Product(

    hash_produto=str(uuid.uuid4()),

    titulo="Mouse Logitech G203",

    preco=Decimal("99.90"),

    status=StatusService.PRONTO

)

product_repo.upsert(produto)

video = Video(

    produto_id=produto.id,

    youtube_id="abc123",

    titulo="Review Logitech G203",

    canal="Canal Teste",

    url="https://youtube.com/watch?v=abc123",

    score=95

)

video_repo.upsert(video)

pipeline = PublicationPipeline()

resultado = pipeline.process(produto)

print("=" * 60)
print(resultado.titulo)
print(produto.status)

video_repo.delete(video.id)
product_repo.delete(produto.id)