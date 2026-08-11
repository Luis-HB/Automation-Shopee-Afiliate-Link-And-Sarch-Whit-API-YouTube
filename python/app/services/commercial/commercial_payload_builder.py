from models.commercial.commercial_payload import CommercialPayload
from models.commercial.knowledge import Knowledge
from models.commercial.evidence import Evidence


class CommercialPayloadBuilder:

    # =====================================================

    def build(self, context):

        payload = CommercialPayload()

        payload.product = context.product

        payload.knowledge = self._knowledge(context)

        payload.evidence = self._evidence(context)

        payload.metadata = context.metadata

        return payload

    # =====================================================

    def _knowledge(self, context):

        return Knowledge(

            product=context.product_analysis,

            videos=context.video_analysis,

            ranking=context.ranking_analysis,

            market=context.market_analysis

        )

    # =====================================================

    def _evidence(self, context):

        return Evidence(

            queries=context.queries,

            videos=context.videos

        )

    # =====================================================

    def create(self, context):

        return self.build(context)