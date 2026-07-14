import requests

url = "https://www.promobit.com.br/Redirect/to/2916416/"

html = requests.get(url).text

with open("/app/redirect.html","w",encoding="utf8") as f:
    f.write(html)

print("Arquivo salvo!")