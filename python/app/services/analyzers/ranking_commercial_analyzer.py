from models.commercial.metric import Metric
from models.commercial.ranking_analysis import RankingAnalysis


class RankingCommercialAnalyzer:

    # =====================================================

    def analyze(self, context):

        videos = context.videos or []

        if not videos:

            return RankingAnalysis(

                best_score=Metric(
                    level="LOW",
                    value=0,
                    description="Nenhum vídeo disponível para análise."
                ),

                average_score=Metric(
                    level="LOW",
                    value=0,
                    description="Não foi possível calcular a média."
                ),

                score_dispersion=Metric(
                    level="LOW",
                    value=0,
                    description="Não existem dados suficientes para calcular a dispersão."
                ),

                winner_strength=Metric(
                    level="LOW",
                    value=0,
                    description="Não existe vídeo vencedor."
                ),

                ranking_quality=Metric(
                    level="LOW",
                    value=0,
                    description="Ranking indisponível por falta de vídeos."
                )
            )

        scores = []

        for video in videos:

            score = getattr(
                video,
                "score",
                0
            )

            if score is None:
                score = 0

            scores.append(float(score))

        # -------------------------------------------------
        # Melhor score
        # -------------------------------------------------

        best_score = max(scores)

        # -------------------------------------------------
        # Média
        # -------------------------------------------------

        average_score = sum(scores) / len(scores)

        # -------------------------------------------------
        # Dispersão
        # -------------------------------------------------

        dispersion = max(scores) - min(scores)

        # -------------------------------------------------
        # Força do vencedor
        # -------------------------------------------------

        if len(scores) == 1:

            winner_strength = 100

        else:

            ordered = sorted(
                scores,
                reverse=True
            )

            first = ordered[0]
            second = ordered[1]

            if first <= 0:

                winner_strength = 0

            else:

                winner_strength = (
                    (first - second)
                    / first
                ) * 100

        # -------------------------------------------------
        # Qualidade do ranking
        # -------------------------------------------------

        ranking_quality = self._ranking_quality(
            scores
        )

        return RankingAnalysis(

            best_score=Metric(
                level=self._level(best_score),
                value=best_score,
                description=(
                    "Score do vídeo melhor classificado."
                )
            ),

            average_score=Metric(
                level=self._level(average_score),
                value=round(
                    average_score,
                    2
                ),
                description=(
                    "Score médio dos vídeos analisados."
                )
            ),

            score_dispersion=Metric(
                level=self._dispersion_level(
                    dispersion
                ),
                value=round(
                    dispersion,
                    2
                ),
                description=(
                    "Diferença entre o maior e o menor score."
                )
            ),

            winner_strength=Metric(
                level=self._winner_level(
                    winner_strength
                ),
                value=round(
                    winner_strength,
                    2
                ),
                description=(
                    "Diferença relativa entre o primeiro "
                    "e o segundo colocado."
                )
            ),

            ranking_quality=Metric(
                level=ranking_quality["level"],
                value=ranking_quality["value"],
                description=ranking_quality["description"]
            )
        )

    # =====================================================

    def _ranking_quality(self, scores):

        if not scores:

            return {
                "level": "LOW",
                "value": 0,
                "description": "Ranking sem dados."
            }

        if len(scores) == 1:

            return {
                "level": "LOW",
                "value": 25,
                "description": (
                    "Ranking baseado em apenas um vídeo."
                )
            }

        if len(scores) < 3:

            return {
                "level": "MEDIUM",
                "value": 50,
                "description": (
                    "Poucos vídeos disponíveis para comparação."
                )
            }

        return {
            "level": "HIGH",
            "value": 100,
            "description": (
                "Quantidade de vídeos suficiente "
                "para comparação entre candidatos."
            )
        }

    # =====================================================

    def _level(self, value):

        if value >= 80:
            return "HIGH"

        if value >= 50:
            return "MEDIUM"

        return "LOW"

    # =====================================================

    def _dispersion_level(self, value):

        if value >= 30:
            return "HIGH"

        if value >= 10:
            return "MEDIUM"

        return "LOW"

    # =====================================================

    def _winner_level(self, value):

        if value >= 20:
            return "HIGH"

        if value >= 5:
            return "MEDIUM"

        return "LOW"