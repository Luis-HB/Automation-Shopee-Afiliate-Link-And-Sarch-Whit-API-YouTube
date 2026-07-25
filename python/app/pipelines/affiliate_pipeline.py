import time

from scrapers.shopee_affiliate_scraper import ShopeeAffiliateScraper


class AffiliatePipeline:

    def __init__(self):

        self.scraper = ShopeeAffiliateScraper()

    def execute(

        self,

        keyword="",

        list_type=2,

        sort_type=5,

        limit=20,

        pages=1

    ):

        print("=" * 70)
        print("AFFILIATE PIPELINE")
        print("=" * 70)

        start = time.perf_counter()

        statistics = {

            "products_found": 0,
            "products_processed": 0,
            "products_failed": 0,
            "pages": 0

        }

        page = 1

        while page <= pages:

            print(f"\nProcessando página {page}")

            try:

                products = self.scraper.execute(

                    keyword=keyword,

                    list_type=list_type,

                    sort_type=sort_type,

                    limit=limit,

                    page=page

                )

            except Exception as e:

                print(f"Erro na página {page}: {e}")
                statistics["products_failed"] += 1
                break

            if not products:

                print("Nenhum produto retornado.")

                break

            statistics["pages"] += 1
            statistics["products_found"] += len(products)

            #
            # O ProductPipeline é executado dentro do
            # ShopeeAffiliateScraper.
            #

            statistics["products_processed"] += len(products)

            page += 1

        statistics["total_time"] = round(

            time.perf_counter() - start,

            2

        )

        print("\nResumo da execução")
        print("-" * 70)
        print(f"Páginas processadas : {statistics['pages']}")
        print(f"Produtos encontrados: {statistics['products_found']}")
        print(f"Produtos processados: {statistics['products_processed']}")
        print(f"Falhas             : {statistics['products_failed']}")
        print(f"Tempo total        : {statistics['total_time']} s")
        print("-" * 70)

        return {

            "statistics": statistics

        }