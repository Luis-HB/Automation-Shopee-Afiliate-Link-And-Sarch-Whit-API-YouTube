import json

from services.agent.models.agent_response import AgentResponse


class AgentResponseParser:

    def parse(self, data):

        # -------------------------------------------------
        # Normalização da resposta do n8n
        # -------------------------------------------------

        if isinstance(data, str):

            data = json.loads(data)

        if not isinstance(data, dict):

            raise ValueError(
                "Resposta do agente possui formato inválido."
            )

        # -------------------------------------------------
        # Algumas respostas do n8n podem vir dentro de
        # uma propriedade "output".
        # -------------------------------------------------

        if "output" in data:

            output = data["output"]

            if isinstance(output, str):

                output = json.loads(output)

            if isinstance(output, dict):

                data = output

        # -------------------------------------------------
        # Criação da resposta
        # -------------------------------------------------

        response = AgentResponse()

        response.decision = data.get(
            "decision",
            "REJECT"
        )

        response.score = data.get(
            "score",
            0
        )

        response.confidence = data.get(
            "confidence",
            0
        )

        response.reason = data.get(
            "reason",
            ""
        )

        response.recommendations = data.get(
            "recommendations",
            []
        )

        response.commercial_analysis = data.get(
            "commercial_analysis",
            {}
        )

        response.metadata = data.get(
            "metadata",
            {}
        )

        return response