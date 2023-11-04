from infrastructure.cli_app.controller import CliController
from presentation.cli_app.view_factory import ViewFactory
# As I can understand this is my so called 'Delivery mechanism' or 'IO device'
# that takes an input from the user and calls Сontroller.

class RunnableCli:
    def get_user_input(self) -> tuple:
        first_number: str = input('first_number: ')
        second_number: str = input('second_number: ')
        operator: str = input('operator: ')
        return first_number, second_number, operator

    def run(self) -> None:
        user_input: tuple = self.get_user_input()
        # There is deffinetely something wrong with me
        # passing View into Presenter like this, but
        # I can't think of another way to do it.
        print(
            CliController().process_data(
                user_input, ViewFactory(), 
            )
        )

class CliApp:
    def create_app(self):
        return RunnableCli()
