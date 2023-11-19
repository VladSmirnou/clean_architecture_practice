# The book says that MVC of my GUI should be implmented in the
# Interface adapters layer, but on the scheme 22.2 it shows that the View
# should be in the Presentation layer with a DB, framework, etc.,
# which is kinda confusing.
from infrastructure.cli_app.interfaces.view_interface import ICliView


class CliView(ICliView):
    def render(self, tmpl: str, data: dict) -> str:
        return tmpl % data
