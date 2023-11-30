from abc import ABC, abstractmethod


class CliViewInterface(ABC):
    @abstractmethod
    def render(self, data: dict) -> str: ...
