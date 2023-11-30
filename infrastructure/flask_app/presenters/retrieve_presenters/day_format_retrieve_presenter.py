import itertools
from infrastructure.flask_app.presenters.retrieve_presenters.\
    retrieve_saved_result_presenter import \
    RetrieveSavedResultPresenter


class DayFormatRetrievePresenter(RetrieveSavedResultPresenter):
    @staticmethod
    def format_calc_results(data: list) -> list:
        # [('1 + 4 = 5', datetime.date(2023, 11, 28)), ...] ->
        # ['1 + 2 = 3, date: 00-00', ...]
        formatted_data: list = list(
            itertools.starmap(
                lambda operands, date: (
                    f'{operands}, date: {date.strftime("%d")}'
                ),
                data
            )
        )
        return formatted_data
