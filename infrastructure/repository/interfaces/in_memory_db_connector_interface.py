from abc import ABC, abstractmethod


class I_InMemoryDbConnector(ABC):
    @abstractmethod
    def execute(self, query: str, params: dict) -> dict: ...
