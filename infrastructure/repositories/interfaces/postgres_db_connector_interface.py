from abc import ABC, abstractmethod


class IPostgresDbConnector(ABC):
    @abstractmethod
    def get_saved_calculations(
        self, query: str, params: tuple) -> list: ...

    @abstractmethod
    def save_calculation(
        self, query: str, params: tuple) -> None: ...
