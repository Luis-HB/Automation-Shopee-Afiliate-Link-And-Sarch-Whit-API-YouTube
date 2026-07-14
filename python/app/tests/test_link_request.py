import requests

url = "https://s.shopee.com.br/4qDhlIJY6q"

r = requests.get(
    url,
    allow_redirects=True,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("URL FINAL:")
print(r.url)

print()

print("STATUS:")
print(r.status_code)