from repositories.base_repository import Repository
from models.search_query import SearchQuery


class SearchQueryRepository(Repository):

    def __init__(self):

        super().__init__(
            "search_queries",
            SearchQuery
        )

    # ====================================================
    # Consultas
    # ====================================================

    def find_by_produto(self, produto_id):

        return (
            self.where("produto_id", produto_id)
                .order_by("ordem")
                .get()
        )

    def find_by_status(self, status):

        return (
            self.where("status", status)
                .order_by("created_at", "DESC")
                .get()
        )

    def find_by_provider(self, provider):

        return (
            self.where("provider", provider)
                .order_by("created_at", "DESC")
                .get()
        )

    # ====================================================
    # Arquitetura nova
    # ====================================================

    def find_by_product(self, product_id):

        return self.find_by_produto(product_id)

    # ====================================================
    # Compatibilidade
    # ====================================================

    def buscar_por_produto(self, produto_id):
        return self.find_by_produto(produto_id)

    def buscar_por_status(self, status):
        return self.find_by_status(status)

    def buscar_por_provider(self, provider):
        return self.find_by_provider(provider)