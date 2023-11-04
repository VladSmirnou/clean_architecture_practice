# The book says that MVC of my GUI should be implmented in the 
# Interface adapters layer, but it also shows that View
# should be in the Infrastructure layer with a DB, framework, etc.,
# which is kinda confusing.
from infrastructure.cli_app.view_interface import ICliView


class CliView(ICliView):
    def render(self, data: dict) -> str:
        return f'The result is: {data.get("result")}'
