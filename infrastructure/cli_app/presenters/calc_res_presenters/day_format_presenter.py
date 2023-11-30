import datetime
from infrastructure.cli_app.interfaces.view_interface import CliViewInterface
from infrastructure.cli_app.presenters.calc_res_presenters.\
    calculate_result_presenter import CalculateResultPresenter


class DayFormatPresenter(CalculateResultPresenter):
    def __init__(self, cli_view_obj: CliViewInterface) -> None:
        super().__init__(cli_view_obj)

    @staticmethod
    def format_date(date: datetime.date) -> str:
        return date.strftime('%d')
