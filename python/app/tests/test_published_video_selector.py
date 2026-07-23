from services.publication.published_video_selector import PublishedvideoSelector
from repositories.product_repository import ProductRepository

repo = ProductRepository()

produto = repo.find_by(
    "status",
    "PRONTO"
)

if not produto:

    print("Nenhum produto PRONTO.")

else:

    video = PublishedvideoSelector().select(produto)

    if video:

        print(video.titulo)
        print(video.score)

    else:

        print("Nenhum vídeo encontrado.")