from infrastructure.flask_app.interfaces.\
    calculate_result_controller_interface import \
    CalculateResultControllerInterface
from infrastructure.flask_app.interfaces.\
    calculate_result_and_save_controller_interface import \
    CalculateResultAndSaveControllerInterface
from infrastructure.flask_app.interfaces.\
    get_saved_result_controller_interface import \
    GetSavedResultControllerInterface
from infrastructure.flask_app.controllers.calculate_result_controller import \
    CalculateResultController
from infrastructure.flask_app.controllers.\
    calculate_result_and_save_controller import \
    CalculateResultAndSaveController
from infrastructure.flask_app.controllers.get_saved_result_controller import \
    GetSavedResultController
from infrastructure.flask_app.presenters.calc_res_presenters.\
    day_month_format_presenter import \
    DayMonthFormatPresenter
from infrastructure.flask_app.presenters.retrieve_presenters.\
    day_format_retrieve_presenter import \
    DayFormatRetrievePresenter
from infrastructure.repositories.sql_alc_repo.sql_alc_repo import \
  SqlAlcRepository
# from infrastructure.repositories.postgres_repo.postgres_repository import \
#     PostgresRepository
# from presentation.db.postgres_db.postgres_db_connector import \
#     PostgresDbConnector
# from presentation.db.postgres_db.postgres_db import SetupPostgresDb
from use_cases.calculate_result import CalculateResult
from use_cases.calculate_result_and_save import CalculateResultAndSave
from use_cases.get_saved_results import RetrievePrevCalculations


class ControllerObjectCreator:
    @staticmethod
    def make_calc_res_contr() -> CalculateResultControllerInterface:
        controller: CalculateResultControllerInterface = (
            CalculateResultController(
                use_case=CalculateResult(
                    presenter=DayMonthFormatPresenter()
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
                    presenter=DayMonthFormatPresenter(),
                    repository=SqlAlcRepository()
                )
            )
        )
        return controller

    @staticmethod
    def make_get_saved_res_contr() -> GetSavedResultControllerInterface:
        controller: GetSavedResultControllerInterface = (
            GetSavedResultController(
                use_case=RetrievePrevCalculations(
                    presenter=DayFormatRetrievePresenter(),
                    repository=SqlAlcRepository()
                )
            )
        )
        return controller
