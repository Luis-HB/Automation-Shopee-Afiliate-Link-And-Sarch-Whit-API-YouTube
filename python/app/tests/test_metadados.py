from bs4 import BeautifulSoup
import requests

url = "https://www.promobit.com.br/oferta/kit-acessorios-banheiro-inox-quadrado-4-pecas-2916416/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, "lxml")

print("=" * 80)
print("METADADOS")
print("=" * 80)

for meta in soup.find_all("meta"):

    if meta.get("property") or meta.get("name"):

        print(
            meta.get("property") or meta.get("name"),
            "=>",
            meta.get("content")
        )