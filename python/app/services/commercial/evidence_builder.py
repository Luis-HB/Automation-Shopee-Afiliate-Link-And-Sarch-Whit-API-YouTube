from ShopeeAffiliate.python.app.models.commercial.evidence import Evidence


class EvidenceBuilder:

    # =====================================================

    def build(self, context):

        evidence = Evidence()

        evidence.queries = context.queries

        evidence.videos = context.videos

        return evidence

    # =====================================================

    def create(self, context):

        return self.build(context)