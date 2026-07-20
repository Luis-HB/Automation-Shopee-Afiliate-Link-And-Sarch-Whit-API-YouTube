from core.clients.graphql_client import GraphQLClient


class ShopeeProductService:

    def __init__(self):

        self.client = GraphQLClient()

    def get_item(self, item_id):

        # Implementaremos depois

        raise NotImplementedError