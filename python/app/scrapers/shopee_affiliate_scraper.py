from services.affiliate_service import AffiliateService
from factories.produto_factory import ProdutoFactory
from repositories.produto_repository import ProdutoRepository


class ShopeeAffiliateScraper:

    def __init__(self):

        self.api = AffiliateService()

        self.repo = ProdutoRepository()

        self.pipeline = ProductPipeline()

    def executar(

        self,

        keyword="",

        list_type=2,

        sort_type=5,

        limite=20,

        page=1

    ):

        produtos_api = self.api.buscar_produtos(

            keyword=keyword,

            listType=list_type,

            sortType=sort_type,

            page=page,

            limit=limite

        )

        produtos = []

        print(f"\n{len(produtos_api)} produtos encontrados.\n")

        for dados in produtos_api:

            try:

                produto = ProdutoFactory.from_affiliate_api(
                    dados
                )

                self.repo.upsert(produto)

                print(f"✔ Produto salvo: {produto.titulo}")

                if processar_videos:

                    contexto = self.pipeline.processar(
                        produto
                    )

                    print(
                        f"   {len(contexto.videos)} vídeos encontrados."
                    )

                produtos.append(produto)

            except Exception as e:

                print(
                    f"Erro ao processar produto: {e}"
                )

        return produtos