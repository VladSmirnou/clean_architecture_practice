import psycopg2
from typing import Union, Any


DSN: str = (
    'host=localhost '
    'dbname=applicationdb '
    'user=postgres '
    'password=NmLo12b#1%^qB@ '  # CUT ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT OUUUUUUTTTTTT
    'port=5432'
)


class SetupPostgresDb:
    db_instance: Union['SetupPostgresDb', None] = None
    conn: Any
    cur: Any

    def __new__(cls, *args, **kwargs) -> 'SetupPostgresDb':
        if not cls.db_instance:
            cls.db_instance = super().__new__(cls)
            cls.db_instance.conn = psycopg2.connect(dsn=DSN)
            cls.db_instance.cur = cls.db_instance.conn.cursor()
        return cls.db_instance

    def create_tables(self) -> None:
        self.cur.execute("""create table if not exists calculations (
            results text
        );
        """)
        self.conn.commit()

    def close_resourses(self):
        self.conn.close()
        self.cur.close()


SetupPostgresDb().create_tables()
