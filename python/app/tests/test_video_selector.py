from repositories.produto_repository import ProdutoRepository
from repositories.video_repository import VideoRepository

from services.video_selector import VideoSelector


produto = ProdutoRepository().all()[0]

videos = VideoRepository().find_by_produto(produto.id)

melhor = VideoSelector.escolher(videos)

print("=" * 80)

print(produto.titulo)

print()

print(melhor.titulo)

print(melhor.score)