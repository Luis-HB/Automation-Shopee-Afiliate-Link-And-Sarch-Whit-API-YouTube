from abc import ABC
from abc import abstractmethod


class BaseVideoProvider(ABC):

    @abstractmethod
    def buscar(
        self,
        consultas
    ):
        pass