from abc import ABC, abstractmethod


class IFlaskController(ABC):
    @abstractmethod
    def process_data(self, data: dict) -> dict: ...
