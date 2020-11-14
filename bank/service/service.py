from .db import DB
from .parser import Parser
from config.db_config import host, username, password, database


class Service:

    def __init__(self):
        self.db = DB(host, username, password, database)
        self.parser = Parser()

    def get_accounts_json(self):
        accounts_info = self.db.get_accounts()
        accounts_json = self.parser.parse_list_info_to_json(accounts_info, entity_type='account')
        return accounts_json

    def get_account_info_json(self, account_id):
        account_info = self.db.get_account(account_id)
        account_json = self.parser.parse_account_item_info_to_json(account_info)
        return account_json

    def get_transactions_json(self, account_id):
        transactions_info = self.db.get_transactions(account_id)
        transactions_json = self.parser.parse_list_info_to_json(transactions_info, entity_type='transaction')
        return transactions_json

    def work_with_money(self, json, operation_type='withdraw'):
        money_operation_dict = Parser.parse_json_to_dict(json)
        if money_operation_dict['sum'] < 0:
            raise ValueError('Sum of money must be more than 0!')
        self.db.work_with_money(money_operation_dict['accountId'], money_operation_dict['sum'], operation_type)

    def close_account(self, json):
        account_dict = Parser.parse_json_to_dict(json)
        self.db.close_account(account_dict['accountId'])
