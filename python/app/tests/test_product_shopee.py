import requests

from scrapers.offer import OfferParser
from scrapers.redirect_parser import RedirectParser

URL = "https://www.promobit.com.br/oferta/kit-acessorios-banheiro-inox-quadrado-4-pecas-2916416/"

# Página da oferta
html = requests.get(URL).text

data = OfferParser.parse(html)

print("=" * 80)
print("TITLE")
print(data["title"])

print("=" * 80)
print("REDIRECT")
print(data["redirect"])

print("=" * 80)

# Link afiliado da Shopee
link = RedirectParser.get_shopee_link(data["redirect"])

print("AFFILIATE LINK")
print(link)

print("=" * 80)

# Segue todos os redirects
r = requests.get(
    link,
    allow_redirects=True,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("FINAL URL")
print(r.url)

print("=" * 80)

print("First 1500 characters of the page:")

print(r.text[:1500])