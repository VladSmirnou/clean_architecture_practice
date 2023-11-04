from infrastructure.cli_app.presenter import CliPresenter
from infrastructure.cli_app.controller_interface import ICliController
from infrastructure.cli_app.view_factory_interface import IViewFactory
from use_cases.use_case import UseCase


class CliController(ICliController):
    def make_use_case_obj(self, view_factory: IViewFactory) -> UseCase:
        return UseCase(
            presenter=CliPresenter(
                view_factory=view_factory
            )
        )

    def process_data(self, data: tuple, view_factory: IViewFactory) -> str:
        user_input: dict = {
            'number_one': int(data[0]),
            'number_two': int(data[1]),
            'operator': data[2],
        }
        use_case_obj = self.make_use_case_obj(view_factory)
        return use_case_obj.process_user_input(user_input)
