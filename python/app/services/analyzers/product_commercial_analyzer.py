class ProductCommercialAnalyzer:

    # =====================================================

    def analyze(self, context):

        produto = context.produto

        analysis = {

            "commercial_score": self._commercial_score(produto),

            "price_position": self._price_position(produto),

            "social_proof": self._social_proof(produto),

            "sales_strength": self._sales_strength(produto),

            "rating_quality": self._rating_quality(produto),

            "discount_strength": self._discount_strength(produto)

        }

        return analysis

    # =====================================================

    def _commercial_score(self, produto):

        score = produto.get("score", 0)

        if score >= 90:
            return "EXCELLENT"

        if score >= 75:
            return "HIGH"

        if score >= 60:
            return "GOOD"

        if score >= 40:
            return "LOW"

        return "VERY_LOW"

    # =====================================================

    def _social_proof(self, produto):

        vendas = produto.get("vendas", 0)

        if vendas >= 10000:
            return "VERY_HIGH"

        if vendas >= 3000:
            return "HIGH"

        if vendas >= 500:
            return "MEDIUM"

        return "LOW"

    # =====================================================

    def _rating_quality(self, produto):

        nota = produto.get("nota", 0)

        if nota >= 4.8:
            return "EXCELLENT"

        if nota >= 4.5:
            return "HIGH"

        if nota >= 4.0:
            return "GOOD"

        return "LOW"

    # =====================================================

    def _discount_strength(self, produto):

        desconto = produto.get("desconto", 0)

        if desconto >= 50:
            return "VERY_HIGH"

        if desconto >= 30:
            return "HIGH"

        if desconto >= 15:
            return "MEDIUM"

        return "LOW"

    # =====================================================

    def _sales_strength(self, produto):

        vendas = produto.get("vendas", 0)

        if vendas >= 50000:
            return "BEST_SELLER"

        if vendas >= 10000:
            return "STRONG"

        if vendas >= 1000:
            return "GOOD"

        return "WEAK"

    # =====================================================

    def _price_position(self, produto):

        preco = produto.get("preco", 0)

        if preco <= 50:
            return "LOW_COST"

        if preco <= 150:
            return "MID_RANGE"

        if preco <= 500:
            return "PREMIUM"

        return "HIGH_END"