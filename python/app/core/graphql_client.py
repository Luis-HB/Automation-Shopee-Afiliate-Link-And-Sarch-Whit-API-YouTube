import json  # Certifique-se de importar o json no topo do arquivo
import requests

from core.config import SHOPEE_CONFIG
from core.shopee_auth import ShopeeAuth


class GraphQLClient:

    def __init__(self):
        self.endpoint = SHOPEE_CONFIG["endpoint"]
        self.auth = ShopeeAuth(
            SHOPEE_CONFIG["app_id"],
            SHOPEE_CONFIG["secret"]
        )

    def execute(
        self,
        query,
        variables=None,
        operation_name=None
    ):
        body = {
            "query": query,
            "variables": variables or {}
        }

        if operation_name:
            body["operationName"] = operation_name

        # 1. Geramos os headers passando o dicionário (como seu auth espera)
        headers = self.auth.build_headers(body)

        # 2. Serializamos o corpo exatamente da mesma forma que o auth faz internamente
        serialized_body = json.dumps(
            body, 
            separators=(",", ":"), 
            ensure_ascii=False
        )

        # 3. Enviamos o payload bruto codificado em UTF-8 usando o parâmetro 'data'
        response = requests.post(
            self.endpoint,
            data=serialized_body.encode("utf-8"),  # <-- Mudança crucial aqui!
            headers=headers,
            timeout=30
        )

        response.raise_for_status()
        payload = response.json()

        if payload.get("errors"):
            raise Exception(payload["errors"])

        return payload["data"]