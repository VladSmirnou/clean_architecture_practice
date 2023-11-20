from use_cases.interfaces.repo_interface import IRepository
from infrastructure.repository.models.sql_alc_models import db, Calculation


class SqlAlcRepository(IRepository):
    def get_saved_calculations(self, amount: int, flag: str) -> list:
        # I don't rly care if it works for now; added just for presentation
        # purposes.
        calculations = Calculation.query.all()
        return calculations

    def save_calculation(self, data: dict) -> None:
        row = f'{data["number_one"]} {data["operator"]} {data["number_two"]} = {data["output"]}'
        new_row = Calculation(results=row)
        db.session.add(new_row)
        db.session.commit()
