from models.search_config import SearchConfig

from core.clients.graphql_client import GraphQLClient
from core.graphql.graphql_loader import GraphQLLoader


class AffiliateService:

    def __init__(self):

        self.client = GraphQLClient()

    def buscar_produtos(self, config: SearchConfig):

        query = GraphQLLoader.load(
            "queries/product_offer.graphql"
        )

        variables = {
            "keyword": config.keyword,
            "page": config.page,
            "limit": config.limit,
            "listType": config.list_type,
            "sortType": config.sort_type,
        }

        if config.shop_id:
            variables["shopId"] = config.shop_id

        if config.item_id:
            variables["itemId"] = config.item_id

        if config.is_key_seller:
            variables["isKeySeller"] = True

        if config.is_ams_offer:
            variables["isAMSOffer"] = True

        if config.shop_types:
            variables["shopType"] = config.shop_types

        data = self.client.execute(
            query=query,
            variables=variables,
            operation_name="ProductOffer"
        )

        return data["productOfferV2"]["nodes"]