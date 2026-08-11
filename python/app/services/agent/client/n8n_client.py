import requests

from services.agent.client.agent_config import AgentConfig


class N8NClient:

    def __init__(self, config: AgentConfig):

        self.config = config

    # =====================================================

    def send(self, request):

        headers = dict(
            self.config.headers or {}
        )

        if self.config.api_key:

            headers["Authorization"] = (
                f"Bearer {self.config.api_key}"
            )

        response = requests.post(

            self.config.webhook_url,

            json=request.to_dict(),

            headers=headers,

            timeout=self.config.timeout,

            verify=self.config.verify_ssl

        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict):

            raise ValueError(
                "n8n retornou uma resposta inválida."
            )

        return data