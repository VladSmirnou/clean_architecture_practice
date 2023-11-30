from abc import ABC, abstractmethod


class GetSavedResultControllerInterface(ABC):
    @abstractmethod
    def process_data(self, data: dict) -> dict: ...
