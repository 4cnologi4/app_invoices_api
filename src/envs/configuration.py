import os
from dotenv import load_dotenv

load_dotenv()


class Configuration:
    def __init__(self):
        self._HOST = os.getenv("HOST")
        self._USER = os.getenv("USER")
        self._PORT = os.getenv("PORT")
        self._DATABASE = os.getenv("DATABASE")
        self._PASSWORD = os.getenv("PASSWORD")
        self._INVOICE_TABLE = os.getenv("INVOICE_TABLE")

    @property
    def HOST(self):
        return self._HOST

    @property
    def USER(self):
        return self._USER

    @property
    def PORT(self):
        return self._PORT

    @property
    def DATABASE(self):
        return self._DATABASE

    @property
    def PASSWORD(self):
        return self._PASSWORD

    @property
    def INVOICE_TABLE(self):
        return self._INVOICE_TABLE
