from services.product.product_analyzer import ProductAnalyzer


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

        texto_base = " ".join(base).strip()

        if not texto_base:
            texto_base = produto.titulo

        consultas = [
            f"{texto_base} {sufixo}"
            for sufixo in SearchQueryBuilder.SUFIXOS
        ]
        #Remove duplicates while preserving order
        return list(dict.fromkeys(consultas))