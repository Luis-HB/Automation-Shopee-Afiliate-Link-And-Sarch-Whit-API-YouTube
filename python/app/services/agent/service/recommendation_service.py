from services.agent.payload.ai_payload_builder import AIPayloadBuilder
from services.agent.client.n8n_client import N8NClient
from services.agent.parser.agent_response_parser import AgentResponseParser
from services.agent.models.agent_request import AgentRequest


class RecommendationService:

    def __init__(self, config):

        self.payload_builder = AIPayloadBuilder()

        self.client = N8NClient(config)

        self.parser = AgentResponseParser()

    # =====================================================

    def analyze(
        self,
        commercial_context,
        agent="commercial-analysis"
    ):

        payload = self.payload_builder.build(
            commercial_context
        )

        request = AgentRequest(
            agent=agent,
            payload=payload.to_dict()
        )

        response = self.client.send(
            request
        )

        return self.parser.parse(
            response
        )

    # =====================================================

    def executar(self, *args, **kwargs):

        return self.analyze(*args, **kwargs)