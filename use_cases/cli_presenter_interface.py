from abc import ABC, abstractmethod


class IOutputBoundary(ABC):
    @abstractmethod
    def present(self, output: int) -> str: ...
