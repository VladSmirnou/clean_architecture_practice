from abc import ABC, abstractmethod


class ICliView(ABC):
    @abstractmethod
    def render(self, tmpl: str, data: dict) -> str: ...
