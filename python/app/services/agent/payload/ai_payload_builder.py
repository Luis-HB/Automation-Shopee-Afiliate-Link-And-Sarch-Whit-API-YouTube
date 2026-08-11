from dataclasses import asdict

from models.ai_payload import AIPayload


class AIPayloadBuilder:

    # =====================================================

    def build(self, context):

        payload = AIPayload()

        payload.product = self._product(context)

        payload.knowledge = self._knowledge(context)

        payload.evidence = self._evidence(context)

        payload.metadata = self._metadata(context)

        payload.config = self._config()

        return payload

    # =====================================================

    def _product(self, context):

        return context.produto

    # =====================================================

    def _knowledge(self, context):

        return {

            "product": asdict(
                context.product_analysis
            ),

            "videos": asdict(
                context.video_analysis
            ),

            "ranking": asdict(
                context.ranking_analysis
            ),

            "market": asdict(
                context.market_analysis
            )

        }

    # =====================================================

    def _evidence(self, context):

        return {

            "queries": [

                q.to_dict()
                if hasattr(q, "to_dict")
                else q

                for q in context.consultas

            ],

            "videos": [

                v.to_dict()
                if hasattr(v, "to_dict")
                else v

                for v in context.videos

            ]

        }

    # =====================================================

    def _metadata(self, context):

        return context.metadata

    # =====================================================

    def _config(self):

        return {

            "pipeline": "commercial",

            "agent": "commercial-analysis",

            "version": "1.0",

            "language": "pt-BR"

        }

    # =====================================================

    def create(self, context):

        return self.build(context)