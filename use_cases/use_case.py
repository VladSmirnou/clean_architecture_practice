# Как я понял, I_InputBoundary (или input port) защищает 
# Controller от изменений в Interactor, т.к.
# Controller может не использовать функционал
# Interactor полностью и получится так, что Controller также
# зависит от части Interactor, которую он не использует напрямую,
# что нарушает Interface Segregation Principle. Также убирается
# транзитивная зависимость Controller от Entities.

from entities.entities import Calculator
from use_cases.cli_presenter_interface import IOutputBoundary
from use_cases.cli_use_case_interface import I_InputBoundary


class UseCase(I_InputBoundary):
    presenter: IOutputBoundary

    def __init__(self, presenter: IOutputBoundary) -> None:
        self.presenter = presenter

    def make_entity_obj(self) -> Calculator:
        return Calculator()

    def process_user_input(self, input_: dict) -> str:
        calc_obj = self.make_entity_obj()
        output: int = 0
        match input_:
            case {'operator': '+', **rest}:
                output: int = calc_obj.add(**rest)
            case {'operator': '-', **rest}:
                output: int = calc_obj.subtract(**rest)
            case etc:
                ...
        return self.presenter.present(output)
