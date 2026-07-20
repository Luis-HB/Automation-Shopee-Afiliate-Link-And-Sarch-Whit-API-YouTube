import math
import re
from python.app.models import video
from services.title_normalizer import TitleNormalizer

class ScoreService:
    
    MARCAS = [
        "logitech",
        "redragon",
        "razer",
        "hyperx",
        "corsair",
        "dazz",
        "fortrek",
        "multilaser",
        "xiaomi",
        "philips",
        "samsung",
        "lg",
        "intelbras",
        "jbl",
        "apple",
        "baseus",
        "anker"
    ]

    @staticmethod
    def extrair_marca_modelo(titulo):

        texto = titulo.lower()

        marca = None

        for m in ScoreService.MARCAS:

            if m in texto:
                marca = m
                break

        modelo = None

        candidatos = re.findall(r"[A-Za-z]{0,3}\d{2,6}[A-Za-z]{0,3}", titulo)

        if candidatos:
            modelo = candidatos[0].lower()

        return marca, modelo

    @staticmethod
    def calcular(produto, video):

        score = 0

        score += ScoreService.score_similaridade(
            produto,
            video
        )

        score += ScoreService.score_views(video)

        score += ScoreService.score_likes(video)

        score += ScoreService.score_duracao(video)

        return round(score, 2)

    # --------------------------------------
    
    @staticmethod
    def score_views(video):

        views = video.get("views", 0)

        if views >= 1000000:
            return 40

        if views >= 500000:
            return 35

        if views >= 100000:
            return 25

        if views >= 50000:
            return 20

        if views >= 10000:
            return 10

        return 0
    
    @staticmethod
    def score_likes(video):

        likes = video.get("likes", 0)

        if likes >= 100000:
            return 20

        if likes >= 50000:
            return 15

        if likes >= 10000:
            return 10

        if likes >= 1000:
            return 5

        return 0
    
    
    @staticmethod
    def score_duracao(video):

        segundos = video.get("duracao", 0)

        if segundos <= 20:
            return 10

        if segundos <= 40:
            return 8

        if segundos <= 60:
            return 6

        return 0

    @staticmethod
    def score_popularidade(video):

        score = 0

        # usa log para evitar que vídeos gigantes dominem tudo
        score += math.log10(video.get("views", 0) + 1) * 20
        score += math.log10(video.get("likes", 0) + 1) * 15

        return score

    # --------------------------------------

    @staticmethod
    def score_similaridade(produto, video):

        score = 0

        palavras_produto = set(
            TitleNormalizer.normalizar(produto.titulo)
        )

        palavras_video = set(
            TitleNormalizer.normalizar(video.titulo)
        )

        iguais = palavras_produto & palavras_video

        if palavras_produto:

            score += (
                len(iguais)
                /
                len(palavras_produto)
            ) * 100

        return score

    # --------------------------------------

    @staticmethod
    def score_qualidade(video):

        score = 0

        duracao = video.get("duracao", 0)

        if duracao <= 30:
            score += 20

        elif duracao <= 60:
            score += 15

        elif duracao <= 90:
            score += 10

        elif duracao <= 180:
            score += 5

    # --------------------------------------

    @staticmethod
    def score_bonus(video):

        score = 0

        titulo = video.get("titulo", "").lower()

        bonus = {

            "review":15,

            "teste":10,

            "unboxing":10,

            "vale a pena":10,

            "comparativo":8,

            "original":5,

            "comprando":5,

            "recebido":5,

            "funciona":5

        }

        for palavra, valor in bonus.items():

            if palavra in titulo:

                score += valor

        return score