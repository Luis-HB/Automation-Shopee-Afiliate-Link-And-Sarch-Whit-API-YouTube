from repositories.product_repository import ProductRepository


class StatusService:

    NOVO = "NOVO"
    PROCESSANDO = "PROCESSANDO"
    SEM_LINK = "SEM_LINK"
    BUSCANDO_VIDEOS = "BUSCANDO_VIDEOS"
    SEM_VIDEO = "SEM_VIDEO"
    VIDEOS_ENCONTRADOS = "VIDEOS_ENCONTRADOS"
    RANQUEADO = "RANQUEADO"
    PRONTO = "PRONTO"
    PUBLICADO = "PUBLICADO"
    EXPIRADO = "EXPIRADO"
    ERRO = "ERRO"

    @staticmethod
    def update(product, status):

        if product.status == status:
            return product

        product.status = status

        ProductRepository().update(product)

        return product

    @classmethod
    def novo(cls, product):
        return cls.update(product, cls.NOVO)

    @classmethod
    def processando(cls, product):
        return cls.update(product, cls.PROCESSANDO)

    @classmethod
    def sem_link(cls, product):
        return cls.update(product, cls.SEM_LINK)

    @classmethod
    def buscando_videos(cls, product):
        return cls.update(product, cls.BUSCANDO_VIDEOS)

    @classmethod
    def sem_video(cls, product):
        return cls.update(product, cls.SEM_VIDEO)

    @classmethod
    def videos_encontrados(cls, product):
        return cls.update(product, cls.VIDEOS_ENCONTRADOS)

    @classmethod
    def ranqueado(cls, product):
        return cls.update(product, cls.RANQUEADO)

    @classmethod
    def pronto(cls, product):
        return cls.update(product, cls.PRONTO)

    @classmethod
    def publicado(cls, product):
        return cls.update(product, cls.PUBLICADO)

    @classmethod
    def expirado(cls, product):
        return cls.update(product, cls.EXPIRADO)

    @classmethod
    def erro(cls, product):
        return cls.update(product, cls.ERRO)