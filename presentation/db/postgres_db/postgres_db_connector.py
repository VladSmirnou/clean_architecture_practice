import itertools
from presentation.db.postgres_db.postgres_db import SetupPostgresDb
from infrastructure.repository.interfaces.postgres_db_connector_interface import \
    IPostgresDbConnector


class PostgresDbConnector(IPostgresDbConnector):
    session: SetupPostgresDb

    def __init__(self, postgres_instanse: SetupPostgresDb) -> None:
        self.session = postgres_instanse

    def get_saved_calculations(
            self, query: str, params: tuple) -> list:
        self.session.cur.execute(query, params)
        return list(
            itertools.chain.from_iterable(self.session.cur.fetchall())
        )

    def save_calculation(self, query: str, params: tuple) -> None:
        self.session.cur.execute(query, params)
        self.session.conn.commit()
