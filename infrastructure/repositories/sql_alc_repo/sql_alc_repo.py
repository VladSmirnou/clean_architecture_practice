from use_cases.interfaces.repo_interface import RepositoryInterface
from infrastructure.repositories.models.sql_alc_models import db, Calculation
from infrastructure.repositories.sql_alc_repo.sql_alch_spec import SqlAlchSpec


class SqlAlcRepository(RepositoryInterface):
    def get_saved_calculations(self, amount: int, flag: str) -> list:
        # I don't rly care if it works for now; added just for presentation
        # purposes.
        calculations: list = Calculation.query.all()
        return SqlAlchSpec.format_data(calculations)

    def save_calculation(self, data: dict) -> None:
        row = (
            f'{data["number_one"]} '
            f'{data["operator"]} '
            f'{data["number_two"]} = {data["output"]}'
        )
        new_row: Calculation = Calculation(results=row)
        db.session.add(new_row)
        db.session.commit()
