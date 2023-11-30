import datetime
from infrastructure.flask_app.presenters.calc_res_presenters.\
    calculate_result_presenter import \
    CalculateResultPresenter


class DayMonthFormatPresenter(CalculateResultPresenter):
    @staticmethod
    def format_date(date: datetime.date) -> str:
        return date.strftime('%m-%d')
