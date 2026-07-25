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

        #
        # Apenas UMA consulta.
        # O YoutubeService adicionará "shorts".
        #
        return [
            f"{texto_base} review"
        ]

    # ----------------------------------------------------
    # Alias para compatibilidade
    # ----------------------------------------------------

    @staticmethod
    def generate(produto):
        return SearchQueryBuilder.gerar(produto)