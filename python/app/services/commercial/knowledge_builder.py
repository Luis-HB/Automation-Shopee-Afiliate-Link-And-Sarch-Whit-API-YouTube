class KnowledgeBuilder:

    def build(self, context):

        return Knowledge(

            product=context.product_analysis,

            videos=context.video_analysis,

            ranking=context.ranking_analysis,

            market=context.market_analysis

        )