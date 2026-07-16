from core.graphql_client import GraphQLClient
from core.graphql_loader import GraphQLLoader


class AffiliateService:

    def __init__(self):

        self.client = GraphQLClient()

    def buscar_produtos(

        self,

        keyword,

        page=1,

        limit=20,

        list_type=0,

        sort_type=1

    ):

        query = GraphQLLoader.load(
            "product_offer.graphql"
        )

        variables = {

            "keyword": keyword,

            "page": page,

            "limit": limit,

            "listType": list_type,

            "sortType": sort_type

        }

        data = self.client.execute(

            query,

            variables,

            "ProductOffer"

        )

        return data["productOfferV2"]["nodes"]