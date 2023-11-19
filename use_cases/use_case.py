# Как я понял, I_InputBoundary (или input port) защищает 
# Controller от изменений в Interactor, т.к.
# Controller может не использовать функционал
# Interactor полностью и получится так, что Controller также
# зависит от части Interactor, которую он не использует напрямую,
# что нарушает Interface Segregation Principle. Также убирается
# транзитивная зависимость Controller от Entities.

from entities.entities import Calculator
from use_cases.dto.input_dto import InputDto, InputDtoRetrieve
from use_cases.dto.output_dto import OutputDto
from use_cases.interfaces.presenter_interface import IOutputBoundary
from use_cases.interfaces.use_case_interface import I_InputBoundary
from use_cases.interfaces.repo_interface import IRepository


class UseCase(I_InputBoundary):
    presenter: IOutputBoundary
    repository: IRepository
    entity_obj: Calculator

    def __init__(self,
                 presenter: IOutputBoundary,
                 repository: IRepository) -> None:
        self.presenter = presenter
        self.repository = repository
        self.entity_obj = self.make_entity_obj()

    def make_entity_obj(self) -> Calculator:
        return Calculator()

    def calculate_result(self, input_dto: InputDto) -> dict:
        output: int = 0
        match input_dto.to_dict():
            case {'operator': '+', **rest}:
                output: int = self.entity_obj.add(**rest)
            case {'operator': '-', **rest}:
                output: int = self.entity_obj.subtract(**rest)
            case etc:
                ...
        return self.presenter.present(OutputDto(output=output))

    def calculate_result_and_save(self, input_dto: InputDto) -> dict:
        output: int = 0
        data: dict = input_dto.to_dict()
        match data:
            case {'operator': '+', **rest}:
                output: int = self.entity_obj.add(**rest)
                self.repository.save_calculation(data | {'output': output})
            case {'operator': '-', **rest}:
                output: int = self.entity_obj.subtract(**rest)
                self.repository.save_calculation(data | {'output': output})
            case etc:
                ...
        return self.presenter.present(OutputDto(output=output))

    def retrieve_prev_calculations(self,
                                   input_dto: InputDtoRetrieve) -> dict:
        output: list = self.repository.get_saved_calculations(
            amount=input_dto.amount_of_results,
            flag=input_dto.tail_or_head_flag
        )
        return self.presenter.present(OutputDto(output=output))
