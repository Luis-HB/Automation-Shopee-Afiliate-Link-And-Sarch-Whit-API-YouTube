from repositories.base_repository import Repository
from models.product import Product


class ProductRepository(Repository):

    def __init__(self):

        super().__init__(
            "produtos",
            Product
        )

    # =====================================
    # Métodos atuais
    # =====================================

    def find_by_hash(self, hash_produto):

        return self.find_by(
            "hash_produto",
            hash_produto
        )

    def find_by_shopee_id(self, shopee_id):

        return self.find_by(
            "shopee_id",
            shopee_id
        )

    def list_new(self):

        return (
            self.where("status", "NOVO")
                .order_by("id", "DESC")
                .get()
        )

    # =====================================
    # Compatibilidade com código antigo
    # =====================================

    def buscar_por_hash(self, hash_produto):
        return self.find_by_hash(hash_produto)

    def buscar_por_shopee_id(self, shopee_id):
        return self.find_by_shopee_id(shopee_id)

    def listar_novos(self):
        return self.list_new()