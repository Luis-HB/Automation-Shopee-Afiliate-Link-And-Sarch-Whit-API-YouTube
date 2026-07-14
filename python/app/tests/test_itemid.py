import requests

url = "https://shopee.com.br/opaanlp/757423107/21253896539"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

for termo in [
    "757423107",
    "21253896539",
    "shopid",
    "shop_id",
    "itemid",
    "item_id",
]:
    print(termo, termo in html)