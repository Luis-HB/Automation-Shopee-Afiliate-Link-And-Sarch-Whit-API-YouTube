import json

from core.shopee_auth import ShopeeAuth

body = {

    "query": "{ ping }"

}

auth = ShopeeAuth(

    "123456",

    "MEU_SECRET"

)

headers = auth.build_headers(body)

print()

print(headers["Authorization"])

print()

print(json.dumps(body))

print()