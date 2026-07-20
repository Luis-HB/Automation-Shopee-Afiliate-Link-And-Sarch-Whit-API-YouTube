import json

import requests

from core.config.settings import SHOPEE_CONFIG
from core.auth.shopee_auth import ShopeeAuth


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

        headers = self.auth.build_headers(body)

        serialized_body = json.dumps(

            body,

            separators=(",", ":"),

            ensure_ascii=False

        )

        response = requests.post(

            self.endpoint,

            data=serialized_body.encode("utf-8"),

            headers=headers,

            timeout=30

        )

        response.raise_for_status()

        payload = response.json()

        if "errors" in payload:

            raise Exception(payload["errors"])

        if "data" not in payload:

            raise Exception(

                f"Resposta inválida da Shopee: {payload}"

            )

        return payload["data"]