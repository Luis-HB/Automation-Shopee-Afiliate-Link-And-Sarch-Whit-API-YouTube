import os
import requests

from bs4 import BeautifulSoup

from factories.product_factory import ProductFactory
from factories.video_factory import VideoFactory

from repositories.product_repository import ProductRepository
from repositories.video_repository import VideoRepository

from services.video.youtube_service import YouTubeService
from services.search.search_query_builder import SearchQueryBuilder
from services.ranking.video_ranking_service import VideoRankingService
from services.context.product_context_builder import ProductContextBuilder

from scrapers.offer import OfferParser
from scrapers.redirect_parser import RedirectParser


class PromobitScraper:

    BASE_URL = "https://www.promobit.com.br"
    LIST_URL = BASE_URL + "/promocoes/loja/shopee/"

    def list_offers(self):

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

    def get_offer_details(self, url):

        html = requests.get(url).text

        product = OfferParser.parse(html)

        if product.get("redirect"):

            product["url_shopee"] = RedirectParser.get_shopee_link(
                product["redirect"]
            )

        return product

    def execute(self, limit=5):

        contexts = []

        offers = self.list_offers()

        print(f"{len(offers)} offers found.")

        product_repo = ProductRepository()
        video_repo = VideoRepository()

        youtube = YouTubeService()

        for url in offers[:limit]:

            print("=" * 80)
            print("Reading:", url)

            try:

                data = self.get_offer_details(url)

                if data["tipo"] == "CUPOM":

                    print(f"Skipping coupon: {data['titulo']}")
                    continue

                product = ProductFactory.from_dict(data)

                product_repo.upsert(product)

                print(f"✔ Product saved: {product.titulo}")

                if not product.id:

                    print("Product saved without ID.")
                    continue

                # =====================================================
                # Context Builder
                # =====================================================

                builder = ProductContextBuilder()

                builder.product(product)

                builder.metadata(
                    url_promobit=url,
                    url_shopee=product.url_shopee
                )

                # =====================================================
                # Search videos
                # =====================================================

                queries = SearchQueryBuilder.generate(product)

                all_videos = {}

                total_results = 0

                for query in queries:

                    builder.add_query(query)

                    print(f"Searching: {query}")

                    try:

                        results = youtube.search_shorts(
                            query,
                            maxResults=10
                        )

                        total_results += len(results)

                        print(
                            f"   {len(results)} videos found"
                        )

                        for video in results:

                            video_id = video["video_id"]

                            if video_id not in all_videos:

                                all_videos[video_id] = video

                    except Exception as e:

                        print(
                            f"Search error '{query}': {e}"
                        )

                print(
                    f"Unique videos: {len(all_videos)}"
                )

                # =====================================================
                # Ranking
                # =====================================================

                ranking = VideoRankingService.rank(

                    product,

                    list(all_videos.values()),

                    limit=10

                )

                print(f"Top {len(ranking)} videos:")

                # =====================================================
                # Save videos
                # =====================================================

                for video_data in ranking:

                    try:

                        video = VideoFactory.from_dict(
                            video_data,
                            product.id
                        )

                        video_repo.upsert(video)

                        builder.add_video(video)

                        print(
                            f"[{video.score:.1f}] {video.titulo}"
                        )

                    except Exception as e:

                        print(
                            f"Error saving video: {e}"
                        )

                # =====================================================
                # Pipeline metadata
                # =====================================================

                builder.pipeline(

                    scraper="Promobit",

                    queries=len(queries),

                    videos_found=total_results,

                    unique_videos=len(all_videos),

                    videos_saved=len(ranking)

                )

                context = builder.build()

                contexts.append(context)

            except Exception as e:

                print(
                    f"Error processing {url}: {e}"
                )

        return contexts