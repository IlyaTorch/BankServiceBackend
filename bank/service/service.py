from .db import DB
from .parser import Parser
from config.db_config import host, username, password, database


class Service:

    def __init__(self):
        self.db = DB(host, username, password, database)
        self.parser = Parser()

    def get_accounts_json(self):
        accounts_info = self.db.get_accounts()
        accounts_json = self.parser.parse_accounts_info_to_json(accounts_info)
        return accounts_json
