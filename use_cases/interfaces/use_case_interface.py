from abc import ABC, abstractmethod
from use_cases.dto.input_dto import InputDto, InputDtoRetrieve


class I_InputBoundary(ABC):
    @abstractmethod
    def calculate_result(self, input_dto: InputDto) -> dict: ...

    @abstractmethod
    def calculate_result_and_save(
        self, input_dto: InputDto) -> dict: ...

    @abstractmethod
    def retrieve_prev_calculations(
        self, input_dto: InputDtoRetrieve) -> dict: ...
