from bs4 import BeautifulSoup


class OfertaParser:

    @staticmethod
    def parse(html):

        soup = BeautifulSoup(html, "html.parser")

        produto = {}

        # Título
        meta = soup.find("meta", property="og:title")
        produto["titulo"] = meta["content"].strip() if meta else ""

        # Descrição
        meta = soup.find("meta", attrs={"name": "description"})
        produto["descricao"] = meta["content"].strip() if meta else ""

        # Imagem
        meta = soup.find("meta", property="og:image")
        produto["imagem"] = meta["content"].strip() if meta else ""

        # URL da oferta no Promobit
        canonical = soup.find("link", rel="canonical")
        produto["url_produto"] = canonical["href"] if canonical else ""

        # Valores padrão
        produto["preco"] = 0
        produto["preco_original"] = 0
        produto["desconto"] = 0
        produto["nota"] = None
        produto["avaliacoes"] = None
        produto["vendas"] = None
        produto["estoque"] = None
        produto["score"] = 0

        # Link de redirecionamento
        produto["redirect"] = None

        for a in soup.find_all("a", href=True):

            href = a["href"]

            if "/Redirect/to/" in href:

                if href.startswith("/"):
                    href = "https://www.promobit.com.br" + href

                produto["redirect"] = href
                break

        # Classificação da oferta
        titulo = produto["titulo"].lower()

        palavras_cupom = [
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
        
        produto["tipo"] = (
            "CUPOM"
            if any(p in titulo for p in palavras_cupom)
            else "PRODUTO"
        )

        return produto