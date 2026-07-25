import requests

from core.config.settings import N8N_CONFIG


class WebhookPublisher:

    @staticmethod
    def publish(payload):

        response = requests.post(

            N8N_CONFIG["publication_webhook"],

            json=payload,

            timeout=30

        )

        response.raise_for_status()

        return response.json()