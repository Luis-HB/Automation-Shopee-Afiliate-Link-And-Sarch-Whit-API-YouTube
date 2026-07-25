class ProviderManager:

    _providers = {
        "youtube": True,
        "shopee": True,
    }

    @classmethod
    def enabled(cls, provider):

        return cls._providers.get(provider, True)

    @classmethod
    def disable(cls, provider):

        cls._providers[provider] = False

    @classmethod
    def enable(cls, provider):

        cls._providers[provider] = True

    @classmethod
    def reset(cls):

        cls._providers = {
            "youtube": True,
            "shopee": True,
        }