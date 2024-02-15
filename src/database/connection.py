import psycopg2

from src.envs.configuration import Configuration

configuration = Configuration()


class DatabaseConnection:
    def __init__(self):
        self._connection = psycopg2.connect(
            host=configuration.HOST,
            port=configuration.PORT,
            database=configuration.DATABASE,
            user=configuration.USER,
            password=configuration.PASSWORD
        )
        self._cursor = self._connection.cursor()

    def raw_sql_select(self, select_query: str):
        self._cursor.execute(select_query)
        row_headers = [x[0] for x in self._cursor.description]
        results = self._cursor.fetchall()
        dict_data = [dict(zip(row_headers, result)) for result in results]
        self._cursor.close()
        self._connection.close()

        return dict_data
