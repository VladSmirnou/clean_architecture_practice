class PostgresSpec:
    @staticmethod
    def resolve_flag(flag: str) -> str:
        # this is just an example, so I (almost) don't care about the
        # correctness of the data, so offset doesn't rly work properly, etc.
        return 'limit' if flag in ('-h', '') else 'offset'

    @staticmethod
    def format_values(data: dict) -> tuple:
        return (
            f'{data["number_one"]} '
            f'{data["operator"]} '
            f'{data["number_two"]} = {data["output"]}',
        )
