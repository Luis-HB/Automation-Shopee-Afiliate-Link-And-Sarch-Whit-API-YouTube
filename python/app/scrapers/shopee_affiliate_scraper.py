from models.search_config import SearchConfig
from models.affiliate_result import AffiliateResult

from services.affiliate.affiliate_service import AffiliateService

from repositories.product_repository import ProductRepository

from factories.product_factory import ProductFactory

from pipelines.product_pipeline import ProductPipeline


class ShopeeAffiliateScraper:

    def __init__(self):

        self.api = AffiliateService()
        self.repo = ProductRepository()
        self.pipeline = ProductPipeline()

    def executar(
        self,
        keyword="",
        list_type=2,
        sort_type=5,
        limite=20,
        page=1,
        processar_videos=True
    ):

        print("=" * 70)
        print("SHOPEE AFFILIATE SCRAPER")
        print("=" * 70)
        print(f"Página.............: {page}")
        print(f"Limite............: {limite}")
        print(f"Processar vídeos..: {processar_videos}")
        print()

        config = SearchConfig(
            keyword=keyword,
            page=page,
            limit=limite,
            list_type=list_type,
            sort_type=sort_type
        )

        produtos_api = self.api.buscar_produtos(config)

        result = AffiliateResult()

        result.products_found = len(produtos_api)

        print(f"{result.products_found} produtos encontrados.\n")

        for dados in produtos_api:

            try:

                produto = ProductFactory.from_affiliate_api(dados)

                self.repo.upsert(produto)

                print(f"✔ Produto salvo: {produto.titulo}")

                if processar_videos:

                    try:

                        pipeline_result = self.pipeline.process(produto)

                        result.add_pipeline(pipeline_result)

                        print("   Pipeline concluído.")

                    except Exception as erro:

                        print(f"   Erro no pipeline: {erro}")

                        result.add_failure()

                else:

                    result.products_processed += 1

            except Exception as erro:

                print(f"Erro ao processar produto: {erro}")

                result.add_failure()

        return result

    # -----------------------------------------------------
    # Alias compatível
    # -----------------------------------------------------

    def execute(
        self,
        keyword="",
        list_type=2,
        sort_type=5,
        limit=20,
        page=1,
        process_videos=True
    ):

        return self.executar(
            keyword=keyword,
            list_type=list_type,
            sort_type=sort_type,
            limite=limit,
            page=page,
            processar_videos=process_videos
        )