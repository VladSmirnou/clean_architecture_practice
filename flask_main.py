import atexit
from use_cases.use_case import UseCase
from presentation.flask_app.flask_app import init_app
from infrastructure.flask_app.controller.controller import FlaskController
from infrastructure.flask_app.presenter.presenter import FlaskPresenter
from infrastructure.repository.postgres_repo.postgres_repository import \
    PostgresRepository
from presentation.db.postgres_db.postgres_db_connector import \
    PostgresDbConnector
from presentation.db.postgres_db.postgres_db import SetupPostgresDb
from infrastructure.repository.sql_alc_repo.sql_alc_repo import SqlAlcRepository


def handle_script_exit():
    SetupPostgresDb().close_resourses()


if __name__ == '__main__':
    # ------- SQL alchemy && Postgres repository -------
    flask_calculator_app = init_app(
        controller=FlaskController(
            use_case=UseCase(
                presenter=FlaskPresenter(),
                repository=SqlAlcRepository()
            )
        )
    )
    # -------------------------------------

    # ------- Postgres repository -------
    flask_calculator_app = init_app(
        controller=FlaskController(
            use_case=UseCase(
                presenter=FlaskPresenter(),
                repository=PostgresRepository(
                    db_connector=PostgresDbConnector(
                        postgres_instanse=SetupPostgresDb()
                    )
                )
            )
        )
    )
    atexit.register(handle_script_exit)
    # -------------------------------------
    flask_calculator_app.run(debug=True)
