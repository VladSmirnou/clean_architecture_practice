from abc import ABC, abstractmethod
from use_cases.dto.output_dto_retrieve import OutputDtoRetrieve
from use_cases.interfaces.retrieve_saved_result_presenter_interface import \
    OutputBoundaryRetrieveInterface
from infrastructure.cli_app.interfaces.view_interface import CliViewInterface


class RetrieveSavedResultPresenter(OutputBoundaryRetrieveInterface, ABC):
    cli_view_obj: CliViewInterface

    def __init__(self, cli_view_obj: CliViewInterface) -> None:
        self.cli_view_obj = cli_view_obj

    def present(self, output_dto: OutputDtoRetrieve) -> dict:
        view_model: dict = self.make_view_model(output_dto.output)
        return {
            'response': self.cli_view_obj.render(view_model)
        }

    @staticmethod
    @abstractmethod
    def make_view_model(data: list) -> dict: ...
