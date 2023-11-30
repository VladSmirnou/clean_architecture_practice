# This module was actually completely incorrect, because as I
# can understand the Presenter and the 'View' (not the View part
# of the MVP pattern, but rather a 'front-end' displaying mechanism)
# are connected via the ViewModel, but they don't directly
# communicate with each other, so the Presenter doesn't know about
# the View and vice versa.
# Seems like the 'View' on schema 22.2 is a 'frontend-thing' that is able to
# poll the ViewModel (a simple DS) for updates that the Presenter
# will load in, so the 'View' can update a page.

# Because the structure of my Cli app is kinda alike with a web application,
# the ViewModel is more likely to be a dictionary or DTO that contains data
# which will be substituted in an HTML or any other template via any rendering
# mechanism (C style  string formatting in my case) in the View module,
# which is part of the MVP.

# In the REST app the ViewModel might be a JSON doc that is serialized from
# the ViewModel\DTO\any other DS.

# I saw some examples where the Presenter formats the
# output_dto into a ViewModel instance and render a
# template at the same time, but I don't wanna implement that
# because then the Presenter will be responsible for two
# different things.

from abc import ABC, abstractmethod
from use_cases.dto.output_dto import OutputDto
from use_cases.interfaces.presenter_interface import OutputBoundaryInterface
from infrastructure.cli_app.interfaces.view_interface import CliViewInterface
import datetime


class CalculateResultPresenter(OutputBoundaryInterface, ABC):
    cli_view_obj: CliViewInterface

    def __init__(self, cli_view_obj: CliViewInterface) -> None:
        self.cli_view_obj = cli_view_obj

    def present(self, output_dto: OutputDto) -> dict:
        formatted_date: str = self.format_date(output_dto.date)
        view_model: dict = {
            'date': formatted_date,
            'output': output_dto.output
        }
        return {
            'response': self.cli_view_obj.render(view_model)
        }
    # Let's say, for example, that someone wanted to change how the
    # date is formatted. So instead of using the isinstance check, like ->
    # "if isinstance(self, DayFormatPresenter): output_dto.date.strftime('%d')"
    # that violates the Open-closed principle, I'll implement it like this.
    @staticmethod
    @abstractmethod
    def format_date(date: datetime.date) -> str: ...
