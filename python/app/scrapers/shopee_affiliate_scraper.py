from models.search_config import SearchConfig

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

        resultados = []

        print(f"{len(produtos_api)} produtos encontrados.\n")

        for dados in produtos_api:

            try:

                produto = ProductFactory.from_affiliate_api(dados)

                self.repo.upsert(produto)

                print(f"✔ Produto salvo: {produto.titulo}")

                if processar_videos:

                    try:

                        pipeline_result = self.pipeline.process(produto)

                        resultados.append(pipeline_result)

                        print("   Pipeline concluído.")

                    except Exception as erro:

                        print(f"   Erro no pipeline: {erro}")

                else:

                    resultados.append(produto)

            except Exception as erro:

                print(f"Erro ao processar produto: {erro}")

        return resultados

    # -----------------------------------------------------
    # Alias compatível com a arquitetura nova
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