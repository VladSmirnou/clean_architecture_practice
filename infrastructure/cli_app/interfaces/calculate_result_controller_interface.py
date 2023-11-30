from abc import ABC, abstractmethod


class CalculateResultControllerInterface(ABC):
    @abstractmethod
    def process_data(self, data: dict) -> dict: ...
