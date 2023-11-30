from abc import ABC, abstractmethod
from use_cases.dto.output_dto import OutputDto
from use_cases.interfaces.presenter_interface import OutputBoundaryInterface
import datetime


class CalculateResultPresenter(OutputBoundaryInterface, ABC):
    def present(self, output_dto: OutputDto) -> dict:
        formatted_date: str = self.format_date(output_dto.date)
        view_model: dict = {
            'date': formatted_date,
            'output': output_dto.output
        }
        return view_model

    @staticmethod
    @abstractmethod
    def format_date(date: datetime.date) -> str: ...
