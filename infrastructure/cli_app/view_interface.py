from abc import ABC, abstractmethod


class ICliView(ABC):
    @abstractmethod
    def render(self, data: dict) -> str: ...
