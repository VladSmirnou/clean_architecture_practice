from use_cases.interfaces.cli_repo_interface import I_InMemoryRepository
from infrastructure.repository.interfaces.in_memory_db_connector_interface import I_InMemoryDbConnector


class InMemoryRepository(I_InMemoryRepository):
    def __init__(self, db_connector: I_InMemoryDbConnector) -> None:
        self.db_connector = db_connector

    def get_saved_calculations(self, amount: int, flag: str | None) -> dict:
        return self.db_connector.execute(
            'select * from calculations', params={'amount': amount, 'flag': flag}
        )

    def save_calculation(self, data: dict) -> None:
        self.db_connector.execute('insert into calculations', params=data)
