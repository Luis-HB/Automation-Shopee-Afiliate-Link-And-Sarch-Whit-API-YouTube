from repositories.product_repository import ProductRepository
from repositories.video_repository import VideoRepository
from services.ranking.video_selector import VideoSelector

produtos = ProductRepository().all()

if not produtos:
    print("⚠️ Nenhum produto encontrado no repositório/banco de dados!")
    # Opcional: criar um produto fake aqui para continuar o teste
    exit(1)

produto = produtos[0]

videos = VideoRepository().find_by_produto(produto.id)

if not videos:
    print(f"⚠️ Nenhum vídeo encontrado para o produto '{produto.titulo}' (ID: {produto.id})")
    exit(1)

melhor = VideoSelector.escolher(videos)

print("=" * 80)
print(produto.titulo)
print()
print(melhor.titulo)
print(melhor.score)