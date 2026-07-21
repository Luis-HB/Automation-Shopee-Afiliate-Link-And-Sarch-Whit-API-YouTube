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

        config = SearchConfig(

            keyword=keyword,

            page=page,

            limit=limite,

            list_type=list_type,

            sort_type=sort_type

        )

        produtos_api = self.api.buscar_produtos(config)

        produtos = []

        print(f"\n{len(produtos_api)} produtos encontrados.\n")

        for dados in produtos_api:

            try:

                produto = ProductFactory.from_affiliate_api(dados)

                self.repo.upsert(produto)

                print(f"✔ Produto salvo: {produto.titulo}")

                if processar_videos:

                    contexto = self.pipeline.processar(produto)

                    print(
                        f"   {len(contexto.videos)} vídeos encontrados."
                    )

                produtos.append(produto)

            except Exception as e:

                print(f"Erro ao processar produto: {e}")

        return produtos