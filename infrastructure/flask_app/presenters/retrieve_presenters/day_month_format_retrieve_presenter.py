import itertools
from infrastructure.flask_app.presenters.retrieve_presenters.\
    retrieve_saved_result_presenter import \
    RetrieveSavedResultPresenter


class DayMonthFormatRetrievePresenter(RetrieveSavedResultPresenter):
    @staticmethod
    def format_calc_results(data: list) -> list:
        formatted_data: list = list(
            itertools.starmap(
                lambda operands, date: (
                    f'{operands}, date: {date.strftime("%m-%d")}'
                ),
                data
            )
        )
        return formatted_data
