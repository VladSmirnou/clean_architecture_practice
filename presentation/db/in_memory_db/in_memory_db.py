import itertools


class InMemoryDB:
    def __init__(self) -> None:
        self.previous_calculation_results: dict[str, str] = {
            '1 + 2': '3',
            '2 - 1': '1',
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
                return self.create_list(
                    self.previous_calculation_results
                )[:amount]
            case 'select * from calculations', {'flag': '-t',
                                                'amount': amount}:
                len_ = len(self.previous_calculation_results)
                return self.create_list(
                    self.previous_calculation_results
                )[len_ - amount:]
            case 'insert into calculations', _:
                key = f'{params["number_one"]} {params["operator"]} {params["number_two"]}'
                self.previous_calculation_results.update(
                    {key: params["output"]}
                )
            case _: raise ValueError

    def create_list(self, dict_: dict) -> list:
        return list(
            itertools.starmap(
                lambda operands, res: f'{operands} = {res}', dict_.items()
            )
        )
