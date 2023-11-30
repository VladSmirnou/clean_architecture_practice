from abc import ABC, abstractmethod
from use_cases.dto.input_dto import InputDto


class CalculateResultInterface(ABC):
    @abstractmethod
    def calculate_result(self, input_dto: InputDto) -> dict: ...
