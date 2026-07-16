import os
import requests

from bs4 import BeautifulSoup

from factories.produto_factory import ProdutoFactory
from factories.video_factory import VideoFactory

from repositories.produto_repository import ProdutoRepository
from repositories.video_repository import VideoRepository

from services.youtube_service import YouTubeService
from services.search_query_builder import SearchQueryBuilder
from services.video_ranking_service import VideoRankingService
from services.contexto_produto_builder import ContextoProdutoBuilder

from scrapers.oferta_parser import OfertaParser
from scrapers.redirect_parser import RedirectParser


class PromobitScraper:

    BASE_URL = "https://www.promobit.com.br"
    LIST_URL = BASE_URL + "/promocoes/loja/shopee/"

    def listar_ofertas(self):

        html = requests.get(self.LIST_URL).text

        soup = BeautifulSoup(html, "html.parser")

        links = []

        for a in soup.find_all("a", href=True):

            href = a["href"]

            if "/oferta/" in href:

                if href.startswith("/"):
                    href = self.BASE_URL + href

                links.append(href)

        return list(dict.fromkeys(links))

    def detalhar_oferta(self, url):

        html = requests.get(url).text

        produto = OfertaParser.parse(html)

        if produto.get("redirect"):

            produto["url_shopee"] = RedirectParser.get_shopee_link(
                produto["redirect"]
            )

        return produto

    def executar(self, limite=5):

        contextos = []

        ofertas = self.listar_ofertas()

        print(f"Foram encontradas {len(ofertas)} ofertas.")

        repo = ProdutoRepository()
        repo_video = VideoRepository()

        youtube = YouTubeService(
            os.getenv("YOUTUBE_API_KEY")
        )

        for url in ofertas[:limite]:

            print("=" * 80)
            print("Lendo:", url)

            try:

                dados = self.detalhar_oferta(url)

                if dados["tipo"] == "CUPOM":

                    print(f"Ignorando cupom: {dados['titulo']}")
                    continue

                produto = ProdutoFactory.from_dict(dados)

                repo.upsert(produto)

                print(f"✔ Produto salvo: {produto.titulo}")

                if not produto.id:

                    print("Produto salvo sem ID.")
                    continue

                # =====================================================
                # Builder do contexto
                # =====================================================

                builder = ContextoProdutoBuilder()

                builder.produto(produto)

                builder.metadata(
                    url_promobit=url,
                    url_shopee=produto.url_shopee
                )

                # =====================================================
                # Busca vídeos
                # =====================================================

                consultas = SearchQueryBuilder.gerar(produto)

                todos_videos = {}

                total_resultados = 0

                for consulta in consultas:

                    builder.add_consulta(consulta)

                    print(f"Pesquisa: {consulta}")

                    try:

                        resultados = youtube.buscar_shorts(
                            consulta,
                            maxResults=10
                        )

                        total_resultados += len(resultados)

                        print(
                            f"   {len(resultados)} vídeos encontrados"
                        )

                        for video in resultados:

                            video_id = video["video_id"]

                            if video_id not in todos_videos:

                                todos_videos[video_id] = video

                    except Exception as e:

                        print(
                            f"Erro na pesquisa '{consulta}': {e}"
                        )

                print(
                    f"Total de vídeos únicos: {len(todos_videos)}"
                )

                # =====================================================
                # Ranking
                # =====================================================

                ranking = VideoRankingService.rank(

                    produto,

                    list(todos_videos.values()),

                    limite=10

                )

                print(f"Top {len(ranking)} vídeos:")

                # =====================================================
                # Salva vídeos
                # =====================================================

                for dados_video in ranking:

                    try:

                        video = VideoFactory.from_dict(
                            dados_video,
                            produto.id
                        )

                        repo_video.upsert(video)

                        builder.add_video(video)

                        print(
                            f"[{video.score:.1f}] {video.titulo}"
                        )

                    except Exception as e:

                        print(
                            "Erro ao salvar vídeo:",
                            e
                        )

                # =====================================================
                # Estatísticas do pipeline
                # =====================================================

                builder.pipeline(

                    scraper="Promobit",

                    consultas=len(consultas),

                    videos_encontrados=total_resultados,

                    videos_unicos=len(todos_videos),

                    videos_salvos=len(ranking)

                )

                contexto = builder.build()

                contextos.append(contexto)

            except Exception as e:

                print(
                    f"Erro ao processar {url}: {e}"
                )

        return contextos