from entities.entities import Calculator
from use_cases.dto.input_dto import InputDtoRetrieve
from use_cases.dto.output_dto_retrieve import OutputDtoRetrieve
from use_cases.interfaces.retrieve_saved_result_presenter_interface import \
    OutputBoundaryRetrieveInterface
from use_cases.interfaces.repo_interface import RepositoryInterface
from use_cases.interfaces.get_saved_results_interface import \
    GetSavedResultInterface


class RetrievePrevCalculations(GetSavedResultInterface):
    presenter: OutputBoundaryRetrieveInterface
    repository: RepositoryInterface
    entity_obj: Calculator

    def __init__(self,
                 presenter: OutputBoundaryRetrieveInterface,
                 repository: RepositoryInterface) -> None:
        self.presenter = presenter
        self.repository = repository
        self.entity_obj = self.make_entity_obj()

    def make_entity_obj(self) -> Calculator:
        return Calculator()

    def retrieve_prev_calculations(self,
                                   input_dto: InputDtoRetrieve) -> dict:
        output: list = self.repository.get_saved_calculations(
            amount=input_dto.amount_of_results,
            flag=input_dto.tail_or_head_flag
        )
        return self.presenter.present(OutputDtoRetrieve(output=output))
