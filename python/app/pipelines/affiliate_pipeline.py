import time

from models.affiliate_pipeline_result import AffiliatePipelineResult

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

        result = AffiliatePipelineResult()

        page = 1

        while page <= pages:

            print(f"\nProcessando página {page}")

            try:

                pipeline_results = self.scraper.execute(

                    keyword=keyword,

                    list_type=list_type,

                    sort_type=sort_type,

                    limit=limit,

                    page=page

                )

            except Exception as e:

                print(f"Erro na página {page}: {e}")

                result.add_error(e)

                break

            if not pipeline_results:

                print("Nenhum produto retornado.")

                break

            result.pages_processed += 1

            result.products_found += len(pipeline_results)

            for pipeline_result in pipeline_results:

                result.add_result(pipeline_result)

            page += 1

        result.processing_time = round(

            time.perf_counter() - start,

            2

        )

        print("\nResumo da execução")
        print("-" * 70)
        print(f"Páginas processadas : {result.pages_processed}")
        print(f"Produtos encontrados: {result.products_found}")
        print(f"Produtos processados: {result.products_processed}")
        print(f"Produtos com falha : {result.products_failed}")
        print(f"Vídeos encontrados : {result.videos_found}")
        print(f"Vídeos salvos      : {result.videos_saved}")
        print(f"Tempo total        : {result.processing_time} s")
        print("-" * 70)

        return result

    # -------------------------------------------------
    # Alias
    # -------------------------------------------------

    def executar(self, **kwargs):

        return self.execute(**kwargs)