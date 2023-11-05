from infrastructure.cli_app.view_factory_interface import IViewFactory
from infrastructure.cli_app.view_interface import ICliView
from presentation.cli_app.view import CliView


class ViewFactory(IViewFactory):
    def make_view(self) -> ICliView:
        return CliView()