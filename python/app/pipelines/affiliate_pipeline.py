import time

from scrapers.shopee_affiliate_scraper import ShopeeAffiliateScraper
from pipelines.product_pipeline import ProductPipeline


class AffiliatePipeline:

    def __init__(self):

        self.scraper = ShopeeAffiliateScraper()
        self.pipeline = ProductPipeline()

    def execute(

        self,

        keyword="",

        list_type=2,

        sort_type=5,

        limit=20,

        pages=1

    ):

        start = time.perf_counter()

        contexts = []

        statistics = {

            "products_found": 0,

            "products_processed": 0,

            "products_failed": 0,

            "pages": 0

        }

        page = 1

        while page <= pages:

            products = self.scraper.execute(

                keyword=keyword,

                list_type=list_type,

                sort_type=sort_type,

                limit=limit,

                page=page

            )

            if not products:
                break

            statistics["pages"] += 1

            statistics["products_found"] += len(products)

            for product in products:

                try:

                    context = self.pipeline.process(product)

                    contexts.append(context)

                    statistics["products_processed"] += 1

                except Exception as e:

                    print(e)

                    statistics["products_failed"] += 1

            page += 1

        statistics["total_time"] = round(

            time.perf_counter() - start,

            2

        )

        return {

            "statistics": statistics,

            "contexts": contexts

        }