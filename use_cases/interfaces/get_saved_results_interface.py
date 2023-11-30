from abc import ABC, abstractmethod
from use_cases.dto.input_dto import InputDtoRetrieve


class GetSavedResultInterface(ABC):
    @abstractmethod
    def retrieve_prev_calculations(
        self, input_dto: InputDtoRetrieve) -> dict: ...
