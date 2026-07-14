from repositories.base_repository import Repository

from models.produto import Produto


class ProdutoRepository(Repository):

    def __init__(self):

        super().__init__(

            "produtos",

            Produto

        )