from services.product.product_analyzer import ProductAnalyzer


class SearchQueryBuilder:

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

            f"{texto_base} review",

            f"{texto_base} unboxing",

            f"{texto_base} teste",

            f"{texto_base} análise"

        ]

        # remove duplicadas mantendo a ordem
        return list(dict.fromkeys(consultas))

    # ----------------------------------------------------
    # Alias
    # ----------------------------------------------------

    @staticmethod
    def generate(produto):
        return SearchQueryBuilder.gerar(produto)