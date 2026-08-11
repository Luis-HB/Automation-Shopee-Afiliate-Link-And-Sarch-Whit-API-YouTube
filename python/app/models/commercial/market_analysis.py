from dataclasses import dataclass

from models.commercial.metric import Metric


@dataclass
class MarketAnalysis:

    commercial_potential: Metric

    competition: Metric

    confidence: Metric

    content_availability: Metric

    recommendation_strength: Metric