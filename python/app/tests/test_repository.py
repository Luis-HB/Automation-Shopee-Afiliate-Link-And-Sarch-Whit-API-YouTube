from decimal import Decimal
import uuid
from repositories.product_repository import ProductRepository
from models.product import Product




def linha():
    print("=" * 60)


repo = ProductRepository()

linha()
print("1 - INSERINDO PRODUTO")
linha()

hash_produto = str(uuid.uuid4())

produto = Product(
    titulo="Mouse Gamer Logitech G203",
    preco=Decimal("99.90"),
    preco_original=Decimal("149.90"),
    desconto=Decimal("33.35"),
    imagem_principal="https://teste.com/mouse.jpg",
    url_produto="https://shopee.com/produto",
    url_afiliado="",
    hash_produto=hash_produto,
    score=Decimal("8.5"),
    status="NOVO"
)

produto = repo.upsert(produto)

print("ID:", produto.id)
print("Título:", produto.titulo)

linha()
print("2 - BUSCANDO PELO HASH")
linha()

produto = repo.find_by("hash_produto", hash_produto)

print(produto)

linha()
print("3 - ALTERANDO O PREÇO")
linha()

produto.preco = Decimal("89.90")

repo.update(produto)

produto = repo.find_by("hash_produto", hash_produto)

print(produto.preco)

linha()
print("4 - LISTANDO TODOS")
linha()

produtos = repo.all()

for p in produtos:

    print(
        p.id,
        p.titulo,
        p.preco,
        p.status
    )

linha()
print("5 - REMOVENDO")
linha()

repo.delete(produto.id)

produto = repo.find_by("hash_produto", hash_produto)

print(produto)

repo.close()

linha()
print("TESTE FINALIZADO")
linha()