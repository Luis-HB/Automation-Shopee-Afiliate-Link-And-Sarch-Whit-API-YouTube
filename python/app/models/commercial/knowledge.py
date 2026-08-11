from dataclasses import dataclass

from models.commercial.product_analysis import ProductAnalysis
from models.commercial.video_analysis import VideoAnalysis
from models.commercial.ranking_analysis import RankingAnalysis
from models.commercial.market_analysis import MarketAnalysis


@dataclass
class Knowledge:

    product: ProductAnalysis | None = None

    videos: VideoAnalysis | None = None

    ranking: RankingAnalysis | None = None

    market: MarketAnalysis | None = None