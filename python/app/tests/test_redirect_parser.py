from scrapers.redirect_parser import RedirectParser

url = "https://www.promobit.com.br/Redirect/to/2916416/"

print(
    RedirectParser.get_shopee_link(url)
)