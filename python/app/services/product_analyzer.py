import re

from services.title_normalizer import TitleNormalizer


class ProductAnalyzer:

    MARCAS = {

        "logitech",
        "redragon",
        "razer",
        "hyperx",
        "corsair",
        "jbl",
        "xiaomi",
        "philips",
        "anker",
        "baseus",
        "intelbras",
        "samsung",
        "lg",
        "multilaser",
        "fortrek"

    }

    CATEGORIAS = {

        "mouse",
        "teclado",
        "fone",
        "headset",
        "caixa",
        "cadeira",
        "monitor",
        "ssd",
        "memoria",
        "gabinete",
        "microfone",
        "webcam"

    }

    @staticmethod
    def analisar(titulo):

        palavras = TitleNormalizer.normalizar(titulo)

        categoria = None
        marca = None
        modelo = None

        extras = []

        for palavra in palavras:

            if palavra in ProductAnalyzer.MARCAS:

                marca = palavra

            elif palavra in ProductAnalyzer.CATEGORIAS:

                categoria = palavra

            elif re.match(r"[a-z]{0,3}\d{2,6}[a-z]{0,3}", palavra):

                modelo = palavra

            else:

                extras.append(palavra)

        return {

            "categoria": categoria,

            "marca": marca,

            "modelo": modelo,

            "extras": extras

        }
        
    @staticmethod
    def termo_busca(produto):   

        dados = ProductAnalyzer.analisar(produto.titulo)

        partes = []

        if dados["marca"]:
            partes.append(dados["marca"])

        if dados["modelo"]:
            partes.append(dados["modelo"])

        partes.extend(dados["extras"])

        partes.append("review")

        return " ".join(partes)