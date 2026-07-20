from repositories.base_repository import Repository
from models.product import Product


class ProductRepository(Repository):

    def __init__(self):

        super().__init__(
            "produtos",
            Product
        )