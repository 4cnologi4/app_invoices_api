from src.database.connection import DatabaseConnection
from src.envs.configuration import Configuration

configuration = Configuration()


class InvoicesDao:
    def __init__(self):
        self._connection = DatabaseConnection()

    def get_invoices_by_date_range(self, start_date, end_date):
        select_query = (f"SELECT * FROM {configuration.INVOICE_TABLE} "
                        f"WHERE invoice_date BETWEEN '{start_date}' AND '{end_date}';")
        return self._connection.raw_sql_select(select_query)
