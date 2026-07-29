from services.commercial.product_commercial_analyzer import ProductCommercialAnalyzer
from services.commercial.video_commercial_analyzer import VideoCommercialAnalyzer
from services.commercial.ranking_commercial_analyzer import RankingCommercialAnalyzer
from services.commercial.market_commercial_analyzer import MarketCommercialAnalyzer

from models.commercial_context import CommercialContext


class CommercialContextBuilder:

    def __init__(self):

        self.product = ProductCommercialAnalyzer()
        self.video = VideoCommercialAnalyzer()
        self.ranking = RankingCommercialAnalyzer()
        self.market = MarketCommercialAnalyzer()

    # =====================================================

    def build(self, product_context):

        commercial = CommercialContext()

        commercial.product = product_context.produto
        commercial.queries = product_context.consultas
        commercial.videos = product_context.videos

        commercial.product_analysis = self.product.analyze(product_context)
        commercial.video_analysis = self.video.analyze(product_context)
        commercial.ranking_analysis = self.ranking.analyze(product_context)
        commercial.market_analysis = self.market.analyze(product_context)

        commercial.metadata = product_context.metadata

        commercial.metadata["builder"] = {

            "version": "1.0",

            "analyzers": [

                "product",
                "video",
                "ranking",
                "market"

            ]

        }

        return commercial

    # =====================================================

    def create(self, product_context):

        return self.build(product_context)