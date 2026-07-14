from decimal import Decimal

from models.produto import Produto

from repositories.produto_repository import ProdutoRepository

repo = ProdutoRepository()

produto = Produto(

    titulo="Produto Teste",

    preco=Decimal("99.90"),

    preco_original=Decimal("129.90"),

    desconto=23,

    imagem_principal="https://teste.com/img.jpg",

    url_produto="https://teste.com",

    hash_produto="123456789"

)

produto = repo.salvar(produto)

print(produto)

repo.close()