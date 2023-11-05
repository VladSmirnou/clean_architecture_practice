from use_cases.cli_presenter_interface import IOutputBoundary
from infrastructure.cli_app.view_interface import ICliView
from infrastructure.cli_app.view_factory_interface import IViewFactory


class CliPresenter(IOutputBoundary):
    view_factory: IViewFactory

    def __init__(self, view_factory: IViewFactory) -> None:
        self.view_factory = view_factory

    def present(self, output: int) -> str:
        formatted_data: dict = {'result': str(output)}
        view_obj: ICliView = self.view_factory.make_view()
        return view_obj.render(formatted_data)
