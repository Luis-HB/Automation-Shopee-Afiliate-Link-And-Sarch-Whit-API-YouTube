from abc import ABC, abstractmethod


class BaseVideoProvider(ABC):

    name = "provider"

    @abstractmethod
    def search(self, queries):
        pass