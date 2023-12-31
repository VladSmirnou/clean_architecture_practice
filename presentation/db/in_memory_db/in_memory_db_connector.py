from infrastructure.repositories.interfaces.\
    in_memory_db_connector_interface import I_InMemoryDbConnector
from presentation.db.in_memory_db.in_memory_db import InMemoryDB


class InMemoryDbConnector(I_InMemoryDbConnector):
    db_engine: InMemoryDB

    def __init__(self, db_engine: InMemoryDB) -> None:
        self.db_engine = db_engine

    def execute(self, query: str, params: dict) -> list:
        session = self.db_engine.create_session()
        return session.execute(query, params)
