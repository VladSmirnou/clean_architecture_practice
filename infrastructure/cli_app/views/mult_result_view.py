from infrastructure.cli_app.interfaces.view_interface import CliViewInterface
from infrastructure.cli_app.views.cli_templates.templates import \
    retr_saved_res_templ


class RetrieveSavedResultView(CliViewInterface):
    def render(self, data: dict) -> str:
        return retr_saved_res_templ % data
