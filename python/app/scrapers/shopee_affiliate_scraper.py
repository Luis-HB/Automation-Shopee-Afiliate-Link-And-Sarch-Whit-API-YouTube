from services.affiliate.affiliate_service import AffiliateService

from repositories.product_repository import ProductRepository

from factories.product_factory import ProductFactory

from pipelines.product_pipeline import ProductPipeline


class ShopeeAffiliateScraper:

    def __init__(self):

        self.api = AffiliateService()

        self.repo = ProductRepository()

        self.pipeline = ProductPipeline()

    def execute(

        self,

        keyword="",

        list_type=2,

        sort_type=5,

        limit=20,

        page=1,

        process_videos=True

    ):

        products_api = self.api.search_products(

            keyword=keyword,

            list_type=list_type,

            sort_type=sort_type,

            page=page,

            limit=limit

        )

        products = []

        print(f"\n{len(products_api)} products found.\n")

        for data in products_api:

            try:

                product = ProductFactory.from_affiliate_api(
                    data
                )

                self.repo.upsert(product)

                print(f"✔ Product saved: {product.title}")

                if process_videos:

                    context = self.pipeline.process(
                        product
                    )

                    print(
                        f"   {len(context.videos)} videos found."
                    )

                products.append(product)

            except Exception as e:

                print(
                    f"Error processing product: {e}"
                )

        return products