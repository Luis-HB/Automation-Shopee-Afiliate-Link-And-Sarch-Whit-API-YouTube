import hashlib

from repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self):

        self.repo = ProductRepository()

    def gerar_hash(self, produto):

        texto = f"{produto.titulo}|{produto.url_produto}"

        return hashlib.sha256(
            texto.encode()
        ).hexdigest()

    def salvar(self, produto):

        if not produto.hash_produto:

            produto.hash_produto = self.gerar_hash(produto)

        produto.score = self.calcular_score(produto)

        return self.repo.upsert(produto)

    def calcular_score(self, produto):

        score = 0

        if produto.desconto:

            score += float(produto.desconto)

        if produto.nota:

            score += float(produto.nota) * 5

        if produto.vendas:

            score += min(produto.vendas / 100, 20)

        return round(score, 2)