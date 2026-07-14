import requests

url = "https://www.promobit.com.br/Redirect/to/2916416/"

response = requests.get(
    url,
    allow_redirects=False
)

print("STATUS")
print(response.status_code)

print()

print("HEADERS")
print(response.headers)