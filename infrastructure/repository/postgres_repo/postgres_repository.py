from use_cases.interfaces.repo_interface import IRepository
from infrastructure.repository.postgres_repo.postgres_rep_spec import \
    PostgresSpec
from infrastructure.repository.interfaces.postgres_db_connector_interface import \
    IPostgresDbConnector


class PostgresRepository(IRepository):
    db_connector: IPostgresDbConnector

    def __init__(self, db_connector: IPostgresDbConnector) -> None:
        self.db_connector = db_connector

    def get_saved_calculations(self, amount: int, flag: str) -> list:
        return self.db_connector.get_saved_calculations(
            'select * from calculations {head_or_tail} %s'.format(
                head_or_tail=PostgresSpec.resolve_flag(flag)
            ),
            params=(amount,)
        )

    def save_calculation(self, data: dict) -> None:
        self.db_connector.save_calculation(
            'insert into calculations values (%s)',
            params=PostgresSpec.format_values(data)
        )
