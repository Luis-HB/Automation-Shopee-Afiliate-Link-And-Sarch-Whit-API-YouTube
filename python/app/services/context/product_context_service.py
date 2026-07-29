from repositories.product_repository import ProductRepository
from repositories.video_repository import VideoRepository
from repositories.search_query_repository import SearchQueryRepository
from repositories.search_result_repository import SearchResultRepository


class ProductContextService:

    def __init__(self):

        self.products = ProductRepository()

        self.videos = VideoRepository()

        self.queries = SearchQueryRepository()

        self.results = SearchResultRepository()

    # =====================================================

    def build(self, product_id):

        product = self.products.find(product_id)

        if product is None:

            raise ValueError(
                f"Produto {product_id} não encontrado."
            )

        queries = self.queries.find_by_product(
            product_id
        )

        videos = self.videos.find_by_product(
            product_id
        )

        results = []

        for query in queries:

            results.extend(

                self.results.find_by_query(

                    query.id

                )

            )

        return {

            "product": product,

            "queries": queries,

            "videos": videos,

            "results": results

        }

    # =====================================================

    def get(self, product_id):

        return self.build(product_id)