import requests

url = "https://shopee.com.br/opaanlp/757423107/21253896539"

html = requests.get(
    url,
    headers={
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/137.0 Safari/537.36"
        )
    }
).text

for palavra in [
    "__NEXT_DATA__",
    "__INITIAL_STATE__",
    "__NUXT__",
    "item_basic",
    "price",
    "rating",
    "stock",
    "historical_sold",
]:
    print(palavra, palavra in html)