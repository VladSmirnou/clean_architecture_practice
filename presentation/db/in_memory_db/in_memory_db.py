import collections
import datetime


class InMemoryDB:
    def __init__(self) -> None:
        self.previous_calculation_results: dict = {
            '1 + 2': collections.namedtuple(
                'Temp', 'res, date'
            )(res='3', date=datetime.date.today()),
            '2 - 1': collections.namedtuple(
                'Temp', 'res, date'
            )(res='1', date=datetime.date.today()),
        }

    def create_session(self) -> 'InMemoryDB':
        # This session object might be of another class, but it
        # doesn't rly matter, because it is used in the same
        # layer with the 'in_memory_db_connector' module.
        return self

    def execute(self, query: str, params: dict) -> list:
        match query, params:
            case 'select * from calculations', {'flag': '' | '-h',
                                                'amount': amount}:
                return list(
                    self.previous_calculation_results.items()
                )[:amount]
            case 'select * from calculations', {'flag': '-t',
                                                'amount': amount}:
                len_ = len(self.previous_calculation_results)
                return list(
                    self.previous_calculation_results.items()
                )[len_ - amount:]
            case 'insert into calculations', _:
                key = (f'{params["number_one"]} '
                       f'{params["operator"]} '
                       f'{params["number_two"]}')
                self.previous_calculation_results.update(
                    {key: collections.namedtuple(
                        'Temp', 'res, date'
                    )(res=params["output"], date=datetime.date.today())}
                )
            case _: raise ValueError
