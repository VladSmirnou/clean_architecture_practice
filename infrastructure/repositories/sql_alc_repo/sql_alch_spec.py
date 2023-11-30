class SqlAlchSpec:
    @staticmethod
    def format_data(data: list) -> list:
        return [(obj.results, obj.date_calculated) for obj in data]
