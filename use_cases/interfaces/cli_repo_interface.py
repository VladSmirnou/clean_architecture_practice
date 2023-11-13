from abc import ABC, abstractmethod


class I_InMemoryRepository(ABC):
    @abstractmethod
    def get_saved_calculations(self, amount: int, flag: str | None) -> dict: ...

    @abstractmethod
    def save_calculation(self, data: dict) -> None: ...
