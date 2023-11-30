from abc import ABC, abstractmethod
from use_cases.dto.output_dto_retrieve import OutputDtoRetrieve
from use_cases.interfaces.retrieve_saved_result_presenter_interface import \
    OutputBoundaryRetrieveInterface


class RetrieveSavedResultPresenter(OutputBoundaryRetrieveInterface, ABC):
    def present(self, output_dto: OutputDtoRetrieve) -> dict:
        # [('1 + 4 = 5', datetime.date(2023, 11, 28)), ...] ->
        # ['1 + 2 = 3, date: 00-00', ...]
        formatted_results: list = self.format_calc_results(output_dto.output)
        return {
            'response': formatted_results
        }

    @staticmethod
    @abstractmethod
    def format_calc_results(data: list) -> list: ...
