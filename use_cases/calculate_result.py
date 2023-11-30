# I do believe that the UseCases should call the Presenter, because
# on page 91 (under scheme 8.2) the book says ->
# "The first thing to notice is that all the dependencies are source code
# dependencies. An arrow pointing from class A to class B means that the source
# code of class A mentions the name of class B, but class B mentions nothing
# about class A."
# So the Controller clearly knows nothing about the Presenter on scheme 22.2,
# thus, I won't call the Presenter from the Controller either.

# As I can see there are two (maybe more) approaches how to interpret the
# Controller-UseCases-Presenter communication: the former is to
# call the Presenter from the UseCases and the latter is to return
# data from the UseCases to the Controller so it can call the Presenter, which
# is demonstrated on scheme 8.2. Idk which one is better tho, but
# returning data from the UseCases will force the Controller to handle
# that data, so it will be dependent on it. Also as I can remember calling
# something for data and processing it is more like a FP thing, but telling
# something what to do is more OOP thing.

from entities.entities import Calculator
from use_cases.dto.input_dto import InputDto
from use_cases.dto.output_dto import OutputDto
from use_cases.interfaces.presenter_interface import OutputBoundaryInterface
from use_cases.interfaces.calculate_result_interface import \
    CalculateResultInterface


class CalculateResult(CalculateResultInterface):
    presenter: OutputBoundaryInterface
    entity_obj: Calculator

    def __init__(self, presenter: OutputBoundaryInterface) -> None:
        self.presenter = presenter
        self.entity_obj = self.make_entity_obj()

    def make_entity_obj(self) -> Calculator:
        return Calculator()

    def get_result(self, input_dto: InputDto) -> int:
        output: int = self.entity_obj.perform_calculations(
            **input_dto.to_dict()
        )
        return output

    def calculate_result(self, input_dto: InputDto) -> dict:
        # UseCase main methods now have the same name with their classes.
        # I can add the '__call__' method in order to remove this name
        # duplication because those classes basically represent those
        # methods, but idk what to do with their interfaces then.
        output: int = self.get_result(input_dto)
        return self.presenter.present(OutputDto(output=output))
