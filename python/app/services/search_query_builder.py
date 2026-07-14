from services.product_analyzer import ProductAnalyzer


class SearchQueryBuilder:

    SUFIXOS = [
        "review",
        "shorts",
        "unboxing",
        "teste",
        "análise",
        "vale a pena"
    ]

    @staticmethod
    def gerar(produto):

        dados = ProductAnalyzer.analisar(produto.titulo)

        base = []

        if dados["marca"]:
            base.append(dados["marca"])

        if dados["modelo"]:
            base.append(dados["modelo"])

        base.extend(dados["extras"])

        texto_base = " ".join(base)

        consultas = []

        for sufixo in SearchQueryBuilder.SUFIXOS:
            consultas.append(f"{texto_base} {sufixo}")

        # Remove duplicadas preservando a ordem
        return list(dict.fromkeys(consultas))