import time

from services.product.product_analyzer import ProductAnalyzer
from services.search.search_query_builder import SearchQueryBuilder
from services.video.video_discovery_service import VideoDiscoveryService
from services.ranking.video_ranking_service import VideoRankingService
from services.context.product_context_builder import ProductContextBuilder

from repositories.video_repository import VideoRepository
from factories.video_factory import VideoFactory


class ProductPipeline:

    def __init__(self):

        self.analyzer = ProductAnalyzer()
        self.discovery = VideoDiscoveryService()
        self.ranking = VideoRankingService()
        self.video_repo = VideoRepository()

    def process(self, product):

        start = time.perf_counter()

        # -------------------------------------
        # Product analysis
        # -------------------------------------

        self.analyzer.analyze(product)

        context = (
            ProductContextBuilder()
            .product(product)
        )

        # -------------------------------------
        # Generate search queries
        # -------------------------------------

        queries = SearchQueryBuilder.generate(product)

        for query in queries:
            context.add_query(query)

        context.metadata(
            source="affiliate_api",
            queries_generated=len(queries),
            search_strategy="multi_provider"
        )

        # -------------------------------------
        # Video discovery
        # -------------------------------------

        try:

            videos = self.discovery.search(
                queries
            )

        except Exception as e:

            context.metadata(
                video_error=str(e),
                videos_found=0,
                videos_ranked=0,
                videos_saved=0
            )

            return context.build()

        context.metadata(
            videos_found=len(videos),
            providers=self.discovery.provider_names()
        )

        # -------------------------------------
        # Ranking
        # -------------------------------------

        ranking = []

        if videos:

            ranking = self.ranking.rank(
                product,
                videos,
                limit=10
            )

        context.metadata(
            videos_ranked=len(ranking)
        )

        # -------------------------------------
        # Persistence
        # -------------------------------------

        videos_saved = 0

        for data in ranking:

            try:

                video = VideoFactory.from_dict(
                    data,
                    product.id
                )

                self.video_repo.upsert(video)

                context.add_video(video)

                videos_saved += 1

            except Exception as e:

                print(f"Error saving video: {e}")

        elapsed = round(
            time.perf_counter() - start,
            2
        )

        context.metadata(
            videos_saved=videos_saved,
            processing_time=elapsed,
            pipeline="affiliate",
            version="3.0"
        )

        return context.build()