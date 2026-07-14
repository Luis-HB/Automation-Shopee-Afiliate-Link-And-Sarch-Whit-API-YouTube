import re
import requests

url = "https://shopee.com.br/opaanlp/757423107/21253896539"

html = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text

urls = sorted(set(re.findall(r'https://[^"\']+', html)))

for u in urls:
    if "api" in u.lower() or "shopee" in u.lower():
        print(u)