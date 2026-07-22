from bs4 import BeautifulSoup


class OfferParser:

    @staticmethod
    def parse(html):

        soup = BeautifulSoup(html, "html.parser")

        product = {}

        # Title
        meta = soup.find("meta", property="og:title")
        product["title"] = meta["content"].strip() if meta else ""

        # Description
        meta = soup.find("meta", attrs={"name": "description"})
        product["description"] = meta["content"].strip() if meta else ""

        # Image
        meta = soup.find("meta", property="og:image")
        product["image"] = meta["content"].strip() if meta else ""

        # Promobit URL
        canonical = soup.find("link", rel="canonical")
        product["product_url"] = canonical["href"] if canonical else ""

        # Default values
        product["price"] = 0
        product["original_price"] = 0
        product["discount"] = 0
        product["rating"] = None
        product["reviews"] = None
        product["sales"] = None
        product["stock"] = None
        product["score"] = 0

        # Redirect link
        product["redirect"] = None

        for a in soup.find_all("a", href=True):

            href = a["href"]

            if "/Redirect/to/" in href:

                if href.startswith("/"):
                    href = "https://www.promobit.com.br" + href

                product["redirect"] = href
                break

        title = product["title"].lower()

        coupon_words = [
            "cupom",
            "voucher",
            "frete",
            "roleta",
            "cashback",
            "moedas",
            "desconto",
            "ganhe",
            "oferta relâmpago"
        ]

        product["type"] = (
            "COUPON"
            if any(word in title for word in coupon_words)
            else "PRODUCT"
        )

        return product


# Compatibilidade apenas para imports antigos
OfertaParser = OfferParser