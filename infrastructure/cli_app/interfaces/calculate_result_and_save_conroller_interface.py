from abc import ABC, abstractmethod


class CalculateResultAndSaveControllerInterface(ABC):
    @abstractmethod
    def process_data(self, data: dict) -> dict: ...
