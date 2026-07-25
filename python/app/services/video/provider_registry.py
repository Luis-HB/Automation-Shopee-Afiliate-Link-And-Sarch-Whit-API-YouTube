class ProviderRegistry:

    _providers = []

    @classmethod
    def register(cls, provider):

        cls._providers.append(provider)

    @classmethod
    def providers(cls):

        return list(cls._providers)

    @classmethod
    def clear(cls):

        cls._providers.clear()