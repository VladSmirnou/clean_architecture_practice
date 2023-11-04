from abc import ABC, abstractmethod


class ICliController(ABC):
    @abstractmethod
    def process_data(self, data: tuple) -> str: ...
