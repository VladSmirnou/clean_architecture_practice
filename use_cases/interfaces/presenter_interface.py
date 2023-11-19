from abc import ABC, abstractmethod
from use_cases.dto.output_dto import OutputDto


class IOutputBoundary(ABC):
    @abstractmethod
    def present(self, output_dto: OutputDto) -> dict: ...
