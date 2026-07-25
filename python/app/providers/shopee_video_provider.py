from providers.base_video_provider import BaseVideoProvider


class ShopeeVideoProvider(BaseVideoProvider):

    name = "shopee"

    def search(self, queries):
        # TODO:
        # Implementar integração com Shopee Video
        return []

    # Compatibilidade
    def buscar(self, consultas):
        return self.search(consultas)