import time

from models.pipeline_result import PipelineResult

from pipelines.actions.analyze_product_action import AnalyzeProductAction
from pipelines.actions.build_query_action import BuildQueriesAction
from pipelines.actions.discovery_videos_action import DiscoverVideosAction
from pipelines.actions.rank_videos_action import RankVideosAction
from pipelines.actions.save_videos_action import SaveVideosAction
from pipelines.actions.finish_pipeline_action import FinishPipelineAction

from services.status.status_service import StatusService


class ProductPipeline:

    def __init__(self):

        self.analyze = AnalyzeProductAction()
        self.build_queries = BuildQueriesAction()
        self.discovery = DiscoverVideosAction()
        self.ranking = RankVideosAction()
        self.save_videos = SaveVideosAction()
        self.finish_pipeline = FinishPipelineAction()

    # =====================================================
    # Pipeline
    # =====================================================

    def process(self, product):

        start = time.perf_counter()

        self._start(product)

        result = PipelineResult(product)

        # -------------------------------------------------
        # 1 - Analyzer
        # -------------------------------------------------

        self.analyze.execute(product)

        # -------------------------------------------------
        # 2 - Queries
        # -------------------------------------------------

        queries = self._build_queries(
            product,
            result
        )

        # -------------------------------------------------
        # 3 - Discovery
        # -------------------------------------------------

        discovery = self._discover(
            product,
            queries,
            result
        )

        if discovery is None:
            return result

        result.discovery = discovery

        # -------------------------------------------------
        # 4 - Ranking
        # -------------------------------------------------

        ranking = self._rank(
            product,
            discovery,
            result
        )

        if ranking is None:
            return result

        result.ranking = ranking

        # -------------------------------------------------
        # 5 - Persistência
        # -------------------------------------------------

        videos_saved = self._save(
            product,
            ranking,
            result
        )

        # -------------------------------------------------
        # Finalização
        # -------------------------------------------------

        return self._finish(
            product,
            result,
            videos_saved,
            start
        )

    # =====================================================
    # Etapas
    # =====================================================

    def _start(self, product):

        print("=" * 70)
        print(">>> PRODUCT PIPELINE <<<")
        print(product.titulo)
        print("=" * 70)

        StatusService.processando(product)

    def _build_queries(self, product, result):

        print("2 - Queries")

        return self.build_queries.execute(
            product,
            result
        )

    def _discover(self, product, queries, result):

        print("3 - Discovery")

        return self.discovery.execute(
            product,
            queries,
            result
        )

    def _rank(self, product, discovery, result):

        print("4 - Ranking")

        return self.ranking.execute(
            product,
            discovery,
            result
        )

    def _save(self, product, ranking, result):

        print("5 - Saving")

        return self.save_videos.execute(
            product,
            ranking,
            result
        )

    def _finish(
        self,
        product,
        result,
        videos_saved,
        start
    ):

        return self.finish_pipeline.execute(
            product,
            result,
            start,
            videos_saved
        )

    # =====================================================
    # Alias
    # =====================================================

    def processar(self, product):
        return self.process(product)