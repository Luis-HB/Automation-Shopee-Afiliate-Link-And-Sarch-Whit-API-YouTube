from dataclasses import dataclass

from models.commercial.metric import Metric


@dataclass
class ProductAnalysis:

    commercial_score: Metric

    sales_strength: Metric

    social_proof: Metric

    rating_quality: Metric

    discount_strength: Metric

    price_position: Metric