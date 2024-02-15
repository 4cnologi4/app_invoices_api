from src.database.invoices_dao import InvoicesDao
from src.envs.configuration import Configuration

configuration = Configuration()


class InvoicesController:
    @staticmethod
    def get_invoices_by_date_range(start_date, end_date):
        try:
            invoices_dao = InvoicesDao()
            response = invoices_dao.get_invoices_by_date_range(start_date, end_date)
            return response
        except Exception as err:
            print(f"Something went wrong: {err}")
