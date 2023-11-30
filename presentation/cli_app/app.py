from presentation.cli_app.controller_objects import ControllerObjectCreator
from infrastructure.cli_app.interfaces.\
    calculate_result_controller_interface import \
    CalculateResultControllerInterface
from infrastructure.cli_app.interfaces.\
    calculate_result_and_save_conroller_interface import \
    CalculateResultAndSaveControllerInterface
from infrastructure.cli_app.interfaces.\
    get_saved_result_controller_interface import \
    GetSavedResultControllerInterface


# As I can understand this is my so called 'Delivery mechanism' or 'IO device'
# that takes an input from the user and calls the Сontroller.


class RunnableCli:
    def get_operation_type(self) -> str:
        return input('What do you wanna do?: ')

    def run(self) -> str:
        match self.get_operation_type():
            case 'calculate_result':
                res: dict = self.calculate_result()
            case 'calculate_result_and_save':
                res: dict = self.calculate_result_and_save()
            case 'retrieve_prev_calculations':
                res: dict = self.retrieve_prev_calculations()
            case _:
                print('Operation doesn\'t exist')
                exit()
        return res['response']

    def calculate_result(self) -> dict:
        first_number: str = input('first_number: ')
        second_number: str = input('second_number: ')
        operator: str = input('operator: ')
        user_input: dict[str, str] = {
            'number_one': first_number,
            'number_two': second_number,
            'operator': operator
        }
        controller: CalculateResultControllerInterface = (
            ControllerObjectCreator.make_calc_res_contr()
        )
        return controller.process_data(user_input)

    def calculate_result_and_save(self) -> dict:
        first_number: str = input('first_number: ')
        second_number: str = input('second_number: ')
        operator: str = input('operator: ')
        user_input: dict[str, str] = {
            'number_one': first_number,
            'number_two': second_number,
            'operator': operator,
        }
        # Чето мне кажется очень жирно создавать такие объекты на
        # каждый реквест, надо бы их предсоздавать и хранить где-то.
        controller: CalculateResultAndSaveControllerInterface = (
            ControllerObjectCreator.make_calc_res_and_save_contr()
        )
        return controller.process_data(user_input)

    def retrieve_prev_calculations(self) -> dict:
        amount_of_results: str = input(
            'How many results do you want to retrieve?: '
        )
        tail_or_head_flag: str = input(
            'From the head or tail? (-h is a default) [-h/-t]: '
        )
        user_input: dict[str, str] = {
            'amount_of_results': amount_of_results,
            'tail_or_head_flag': tail_or_head_flag
        }
        controller: GetSavedResultControllerInterface = (
            ControllerObjectCreator.make_get_saved_res_contr()
        )
        return controller.process_data(user_input)


class CliApp:
    def create_app(self) -> RunnableCli:
        return RunnableCli()
