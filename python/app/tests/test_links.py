from bs4 import BeautifulSoup
import requests

url = "https://www.promobit.com.br/oferta/kit-acessorios-banheiro-inox-quadrado-4-pecas-2916416/"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

soup = BeautifulSoup(html, "lxml")

print("=" * 80)
print("LINKS")
print("=" * 80)

for a in soup.find_all("a", href=True):

    texto = a.get_text(strip=True)

    if texto:
        print(texto, "=>", a["href"])