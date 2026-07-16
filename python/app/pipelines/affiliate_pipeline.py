import time

from scrapers.shopee_affiliate_scraper import ShopeeAffiliateScraper
from pipelines.product_pipeline import ProductPipeline


class AffiliatePipeline:

    def __init__(self):

        self.scraper = ShopeeAffiliateScraper()

        self.pipeline = ProductPipeline()

    def executar(

        self,

        keyword="",

        list_type=2,

        sort_type=5,

        limite=20,

        paginas=1

    ):

        inicio = time.perf_counter()

        contextos = []

        estatisticas = {

            "produtos_encontrados": 0,

            "produtos_processados": 0,

            "produtos_falharam": 0,

            "paginas": 0

        }

        pagina = 1

        while pagina <= paginas:

            produtos = self.scraper.executar(

                keyword=keyword,

                list_type=list_type,

                sort_type=sort_type,

                limite=limite,

                page=pagina

            )

            if not produtos:

                break

            estatisticas["paginas"] += 1

            estatisticas["produtos_encontrados"] += len(produtos)

            for produto in produtos:

                try:

                    contexto = self.pipeline.processar(produto)

                    contextos.append(contexto)

                    estatisticas["produtos_processados"] += 1

                except Exception as e:

                    print(e)

                    estatisticas["produtos_falharam"] += 1

            pagina += 1

        estatisticas["tempo_total"] = round(

            time.perf_counter() - inicio,

            2

        )

        return {

            "estatisticas": estatisticas,

            "contextos": contextos

        }