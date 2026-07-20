from abc import ABC, abstractmethod


class BaseVideoProvider(ABC):

    @abstractmethod
    def search(self, queries):
        pass