from services.product.product_analyzer import ProductAnalyzer


class AnalyzeProductAction:

    def __init__(self):

        self.analyzer = ProductAnalyzer()

    def execute(self, product):

        print("1 - Analyzer")

        self.analyzer.analyze(product)

        return product

    # -----------------------------------------
    # Compatibilidade
    # -----------------------------------------

    def process(self, product):
        return self.execute(product)

    def executar(self, product):
        return self.execute(product)