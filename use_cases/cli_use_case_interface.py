from abc import ABC, abstractmethod


class I_InputBoundary(ABC):
    @abstractmethod
    def process_user_input(self, input_: dict) -> str: ...
