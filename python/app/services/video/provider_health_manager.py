from datetime import datetime


class ProviderHealthManager:

    _providers = {
        "youtube": {
            "enabled": True,
            "reason": None,
            "updated_at": None
        },
        "shopee": {
            "enabled": True,
            "reason": None,
            "updated_at": None
        }
    }

    @classmethod
    def is_enabled(cls, provider):

        provider = cls._providers.get(provider)

        if provider is None:
            return True

        return provider["enabled"]

    @classmethod
    def disable(cls, provider, reason=None):

        cls._providers.setdefault(provider, {})

        cls._providers[provider]["enabled"] = False
        cls._providers[provider]["reason"] = reason
        cls._providers[provider]["updated_at"] = datetime.now()

    @classmethod
    def enable(cls, provider):

        cls._providers.setdefault(provider, {})

        cls._providers[provider]["enabled"] = True
        cls._providers[provider]["reason"] = None
        cls._providers[provider]["updated_at"] = datetime.now()

    @classmethod
    def reason(cls, provider):

        provider = cls._providers.get(provider)

        if provider is None:
            return None

        return provider["reason"]

    @classmethod
    def info(cls, provider):

        return cls._providers.get(provider)

    @classmethod
    def all(cls):

        return cls._providers

    @classmethod
    def reset(cls):

        for provider in cls._providers.values():

            provider["enabled"] = True
            provider["reason"] = None
            provider["updated_at"] = None