from models.commercial.metric import Metric
from models.commercial.market_analysis import MarketAnalysis


class MarketCommercialAnalyzer:

    # =====================================================

    def analyze(self, context):

        commercial = self._commercial_potential(context)

        competition = self._competition(context)

        confidence = self._confidence(context)

        availability = self._content_availability(context)

        recommendation = self._recommendation_strength(

            commercial,

            confidence,

            availability

        )

        return MarketAnalysis(

            commercial_potential=commercial,

            competition=competition,

            confidence=confidence,

            content_availability=availability,

            recommendation_strength=recommendation

        )