from core.graphql_client import GraphQLClient
from core.graphql_loader import GraphQLLoader

from models.search_config import SearchConfig


class AffiliateService:

    def __init__(self):

        self.client = GraphQLClient()

        self.product_offer_query = GraphQLLoader.load(
            "product_offer.graphql"
        )

        self.shop_offer_query = GraphQLLoader.load(
            "shop_offer.graphql"
        )

        self.short_link_query = GraphQLLoader.load(
            "generate_short_link.graphql"
        )

        self.conversion_query = GraphQLLoader.load(
            "conversion_report.graphql"
        )

    def buscar_produtos(
        self,
        config: SearchConfig
    ):

        variables = {
            "keyword": config.keyword,
            "page": config.page,
            "limit": config.limit,
            "listType": config.list_type,
            "sortType": config.sort_type,
        }

        if config.shop_id is not None:
            variables["shopId"] = config.shop_id

        if config.item_id is not None:
            variables["itemId"] = config.item_id

        if config.is_key_seller:
            variables["isKeySeller"] = True

        if config.is_ams_offer:
            variables["isAMSOffer"] = True

        if config.shop_types:
            variables["shopType"] = config.shop_types

        data = self.client.execute(
            query=self.product_offer_query,
            variables=variables,
            operation_name="ProductOffer"
        )

        return data["productOfferV2"]["nodes"]