import requests

from scrapers.offer import OfertaParser
from scrapers.redirect_parser import RedirectParser

URL = "https://www.promobit.com.br/oferta/kit-acessorios-banheiro-inox-quadrado-4-pecas-2916416/"

# Página da oferta
html = requests.get(URL).text

dados = OfertaParser.parse(html)

print("=" * 80)
print("TÍTULO")
print(dados["titulo"])

print("=" * 80)
print("REDIRECT")
print(dados["redirect"])

print("=" * 80)

# Link afiliado da Shopee
link = RedirectParser.get_shopee_link(dados["redirect"])

print("LINK AFILIADO")
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

print("URL FINAL")
print(r.url)

print("=" * 80)

print("Primeiros 1500 caracteres da página:")

print(r.text[:1500])