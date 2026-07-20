import re


class TitleNormalizer:

    STOPWORDS = {

        "mouse",
        "gamer",
        "rgb",
        "review",
        "reviews",
        "short",
        "shorts",
        "oficial",
        "novo",
        "nova",
        "promoção",
        "promocao",
        "oferta",
        "vale",
        "pena",
        "melhor",
        "bom",
        "barato",
        "unboxing",
        "teste",
        "testeando",
        "comprando",
        "compramos",
        "lightsync",
        "wireless",
        "com",
        "para",
        "de",
        "da",
        "do",
        "em",
        "no",
        "na",
        "e"

    }

    @staticmethod
    def normalizar(texto):
        
        if not texto:
            return []

        texto = texto.lower()

        palavras = re.findall(r"[a-z0-9]+", texto)

        palavras = [

            p

            for p in palavras

            if p not in TitleNormalizer.STOPWORDS

        ]

        return palavras