import re
import requests

url = "https://shopee.com.br/opaanlp/757423107/21253896539"

html = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text

apis = sorted(set(re.findall(r'/api/[^"\']+', html)))

print("=" * 80)

for api in apis:
    print(api)
    