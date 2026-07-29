from dataclasses import dataclass

from models.commercial.metric import Metric


@dataclass
class RankingAnalysis:

    best_score: Metric

    average_score: Metric

    score_dispersion: Metric

    winner_strength: Metric

    ranking_quality: Metric