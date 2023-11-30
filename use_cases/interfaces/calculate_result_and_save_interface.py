from abc import ABC, abstractmethod
from use_cases.dto.input_dto import InputDto


class CalculateResultAndSaveInterface(ABC):
    @abstractmethod
    def calculate_result_and_save(
        self, input_dto: InputDto) -> dict: ...
