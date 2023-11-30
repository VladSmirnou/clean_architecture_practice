# Yeah, that's quite a lot of imports, no cap
from infrastructure.cli_app.controllers.calculate_result_controller import \
    CalculateResultController
from infrastructure.cli_app.controllers.\
    calculate_result_and_save_controller import \
    CalculateResultAndSaveController
from infrastructure.cli_app.controllers.get_saved_result_controller import \
    GetSavedResultController
from infrastructure.cli_app.interfaces.\
    calculate_result_controller_interface import \
    CalculateResultControllerInterface
from infrastructure.cli_app.interfaces.\
    calculate_result_and_save_conroller_interface import \
    CalculateResultAndSaveControllerInterface
from infrastructure.cli_app.interfaces.\
    get_saved_result_controller_interface import \
    GetSavedResultControllerInterface
from infrastructure.repositories.in_memory_repo.in_memory_repository import \
    InMemoryRepository
from infrastructure.cli_app.views.single_result_view import \
    CalculateResultView
from infrastructure.cli_app.views.mult_result_view import \
    RetrieveSavedResultView
from presentation.db.in_memory_db.in_memory_db_connector import \
    InMemoryDbConnector
from presentation.db.in_memory_db.in_memory_db import InMemoryDB
from use_cases.calculate_result import CalculateResult
from infrastructure.cli_app.presenters.retrieve_presenters.\
    day_format_retrieve_presenter import \
    DayFormatRetrievePresenter
# Use this presenter or the one above to get different date formatting.
# from infrastructure.cli_app.presenter.\
#     day_month_format_retrieve_presenter import \
#     DayMonthFormatRetrievePresenter
from infrastructure.cli_app.presenters.calc_res_presenters.\
    day_format_presenter import \
    DayFormatPresenter
from infrastructure.cli_app.presenters.calc_res_presenters.\
    day_month_format_presenter import \
    DayMonthFormatPresenter
from use_cases.calculate_result_and_save import CalculateResultAndSave
from use_cases.get_saved_results import RetrievePrevCalculations


class ControllerObjectCreator:
    @staticmethod
    def make_calc_res_contr() -> CalculateResultControllerInterface:
        controller: CalculateResultControllerInterface = (
            CalculateResultController(
                use_case=CalculateResult(
                    presenter=DayFormatPresenter(
                        cli_view_obj=CalculateResultView()
                    )
                )
            )
        )
        return controller

    @staticmethod
    def make_calc_res_and_save_contr(
    ) -> CalculateResultAndSaveControllerInterface:
        controller: CalculateResultAndSaveControllerInterface = (
            CalculateResultAndSaveController(
                use_case=CalculateResultAndSave(
                    presenter=DayMonthFormatPresenter(
                        cli_view_obj=CalculateResultView()
                    ),
                    repository=InMemoryRepository(
                        db_connector=InMemoryDbConnector(
                            db_engine=InMemoryDB()
                        )
                    )
                )
            )
        )
        return controller

    @staticmethod
    def make_get_saved_res_contr(
    ) -> GetSavedResultControllerInterface:
        controller: GetSavedResultControllerInterface = (
            GetSavedResultController(
                use_case=RetrievePrevCalculations(
                    presenter=DayFormatRetrievePresenter(
                        cli_view_obj=RetrieveSavedResultView()
                    ),
                    repository=InMemoryRepository(
                        db_connector=InMemoryDbConnector(
                            db_engine=InMemoryDB()
                        )
                    )
                )
            )
        )
        return controller
