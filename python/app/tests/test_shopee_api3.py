import requests

url = "https://shopee.com.br/opaanlp/757423107/21253896539"

html = requests.get(url).text

for linha in html.splitlines():

    if "api/v4/pdp/get_pc" in linha:

        print(linha)