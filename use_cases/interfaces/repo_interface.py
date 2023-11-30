from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def get_saved_calculations(
        self, amount: int, flag: str) -> list: ...

    @abstractmethod
    def save_calculation(self, data: dict) -> None: ...
