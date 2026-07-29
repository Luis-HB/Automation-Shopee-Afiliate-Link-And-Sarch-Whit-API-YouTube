from datetime import datetime

from models.ai_payload import AIPayload

from services.context.ai_context_serializer import AIContextSerializer


class PayloadBuilder:

    def __init__(self):

        self.serializer = AIContextSerializer()

    # =====================================================

    def build(self, context):

        payload = AIPayload()

        #
        # Dados do produto
        #
        payload.produto = self.serializer.product(
            context
        )

        #
        # Consultas + vídeos
        #
        payload.consultas = self.serializer.queries(
            context
        )

        #
        # Informações do pipeline
        #
        payload.pipeline = {

            "version": "1.0",

            "generated_at": datetime.utcnow().isoformat(),

            "source": "affiliate_pipeline"

        }

        #
        # Estatísticas
        #
        payload.metadata = {

            "total_consultas": len(context.consultas),

            "total_videos": len(context.videos),

            "total_resultados": len(context.resultados),

            "score_produto": context.score_produto

        }

        #
        # Configuração padrão
        #
        payload.config = {

            "language": "pt-BR",

            "marketplace": "Shopee",

            "objective": "Selecionar o melhor vídeo para divulgação.",

            "max_videos": 10

        }

        return payload

    # =====================================================

    def create(self, context):

        return self.build(context)