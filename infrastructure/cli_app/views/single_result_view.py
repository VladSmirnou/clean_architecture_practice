from infrastructure.cli_app.interfaces.view_interface import CliViewInterface
from infrastructure.cli_app.views.cli_templates.templates import \
    calc_res_templ


class CalculateResultView(CliViewInterface):
    def render(self, data: dict) -> str:
        return calc_res_templ % data
