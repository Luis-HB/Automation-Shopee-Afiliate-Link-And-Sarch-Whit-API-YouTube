from services.commercial.commercial_context_builder import CommercialContextBuilder
from services.agents.service.recommendation_service import RecommendationService

from services.status.status_service import StatusService


class CommercialAnalysisAction:

    def __init__(self, agent_config):

        self.context_builder = CommercialContextBuilder()

        self.recommendation = RecommendationService(
            agent_config
        )

    # =====================================================

    def execute(self, product, result):

        print("6 - Análise Comercial IA")

        StatusService.analisando_comercialmente(product)

        context = self.context_builder.build(product)

        response = self.recommendation.analyze(context)

        result.agent_response = response

        result.commercial_context = context

        if response.decision != "APPROVED":

            print("Produto rejeitado pelo agente.")

            StatusService.rejeitado(product)

            return None

        print("Produto aprovado pelo agente.")

        StatusService.aprovado(product)

        return response

    # =====================================================

    def executar(self, *args, **kwargs):

        return self.execute(*args, **kwargs)