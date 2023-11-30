import itertools
import functools
from infrastructure.cli_app.interfaces.view_interface import CliViewInterface
from infrastructure.cli_app.presenters.retrieve_presenters.\
    retrieve_saved_result_presenter import \
    RetrieveSavedResultPresenter


class DayFormatRetrievePresenter(RetrieveSavedResultPresenter):
    def __init__(self, cli_view_obj: CliViewInterface) -> None:
        super().__init__(cli_view_obj)

    @staticmethod
    def make_view_model(data: list) -> dict:
        # data = [('1 + 2', ntuple('3', date_obj)),] -> '1 + 2 = 3, date: 00;'
        formatted_data: str = f'[{functools.reduce(
            lambda accum, new_val: f"{accum}; {new_val}",
            itertools.starmap(
                lambda operands, ntuple_: (
                    f"{operands} = {ntuple_.res}, date: {ntuple_.date.strftime(
                        """%d"""
                    )}"
                ),
                data
            )
        )}]'
        return {'output': formatted_data}
