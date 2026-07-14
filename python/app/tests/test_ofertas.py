from bs4 import BeautifulSoup
import requests

url = "https://www.promobit.com.br/oferta/kit-acessorios-banheiro-inox-quadrado-4-pecas-2916416/"

headers = {

    "User-Agent": "Mozilla/5.0"

}

html = requests.get(

    url,

    headers=headers

).text

print(html[:2000])

soup = BeautifulSoup(html, "lxml")

print("\n\nTÍTULO:")

print(soup.title.text)