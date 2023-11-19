from infrastructure.cli_app.interfaces.controller_interface import \
    ICliController
from infrastructure.cli_app.controller.controller import CliController
from presentation.db.in_memory_db.in_memory_db_connector import \
    InMemoryDbConnector
from presentation.db.in_memory_db.in_memory_db import InMemoryDB
from infrastructure.repository.in_memory_repo.in_memory_repository import \
    InMemoryRepository
from infrastructure.cli_app.presenter.presenter import CliPresenter
from presentation.cli_app.view import CliView
from use_cases.use_case import UseCase


# As I can understand this is my so called 'Delivery mechanism' or 'IO device'
# that takes an input from the user and calls the Сontroller.

class RunnableCli:
    controller: ICliController

    def __init__(self, controller: ICliController) -> None:
        self.controller = controller

    def get_operation_type(self) -> str:
        return input('What do you wanna do?: ')

    def run(self) -> None:
        match self.get_operation_type():
            case 'calculate_result':
                user_input: dict = self.calculate_result()
            case 'calculate_result_and_save':
                user_input: dict = self.calculate_result_and_save()
            case 'retrieve_prev_calculations':
                user_input: dict = self.retrieve_prev_calculations()
            case _:
                print('Operation doesn\'t exist')
                exit()
        print(self.controller.process_data(user_input))

    def calculate_result(self) -> dict:
        first_number: str = input('first_number: ')
        second_number: str = input('second_number: ')
        operator: str = input('operator: ')
        return {
            'number_one': first_number,
            'number_two': second_number,
            'operator': operator
        }

    def calculate_result_and_save(self) -> dict:
        first_number: str = input('first_number: ')
        second_number: str = input('second_number: ')
        operator: str = input('operator: ')
        save: bool = True
        return {
            'number_one': first_number,
            'number_two': second_number,
            'operator': operator,
            'save': save
        }

    def retrieve_prev_calculations(self) -> dict:
        amount_of_results: str = input(
            'How many results do you want to retrieve?: '
        )
        tail_or_head_flag: str = input(
            'From the head or tail? (-h is a default) [-h/-t]: '
        )
        return {
            'amount_of_results': amount_of_results,
            'tail_or_head_flag': tail_or_head_flag
        }


class CliApp:
    def create_app(self) -> RunnableCli:
        return RunnableCli(
            controller=CliController(
                use_case=UseCase(
                    presenter=CliPresenter(
                        cli_view_obj=CliView()
                    ),
                    repository=InMemoryRepository(
                        db_connector=InMemoryDbConnector(
                            db_engine=InMemoryDB()
                        )
                    )
                )
            )
        )
