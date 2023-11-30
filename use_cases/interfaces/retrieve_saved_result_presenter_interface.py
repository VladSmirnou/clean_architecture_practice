from abc import ABC, abstractmethod
from use_cases.dto.output_dto_retrieve import OutputDtoRetrieve


class OutputBoundaryRetrieveInterface(ABC):
    @abstractmethod
    def present(self, output_dto: OutputDtoRetrieve) -> dict: ...
