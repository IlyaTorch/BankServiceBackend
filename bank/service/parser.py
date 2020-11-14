import json
from typing import Tuple, List


class Parser:
    KEYS_FOR_ACCOUNTS_JSON = ["accountId", "opened", "sum"]
    KEYS_FOR_TRANSACTIONS_JSON = ["transactionId", "accountId", "sum"]

    def parse_accounts_info_to_json(self, accounts_info: List[Tuple[int, int, int]]) -> json:
        accounts = []
        for account_row in accounts_info:
            account_id, opened, account_sum = account_row
            account_dict = {
                self.KEYS_FOR_ACCOUNTS_JSON[0]: account_id,
                self.KEYS_FOR_ACCOUNTS_JSON[1]: opened,
                self.KEYS_FOR_ACCOUNTS_JSON[2]: account_sum
            }
            accounts.append(account_dict)

        return json.dumps(accounts, indent=3)

    def parse_account_item_info_to_json(self, account_row: List[Tuple[int, int, int]]) -> json:
        # list always contains one element
        account_id, opened, account_sum = account_row[0]
        account_dict = {
            self.KEYS_FOR_ACCOUNTS_JSON[0]: account_id,
            self.KEYS_FOR_ACCOUNTS_JSON[1]: opened,
            self.KEYS_FOR_ACCOUNTS_JSON[2]: account_sum
        }

        return json.dumps(account_dict, indent=3)

    def parse_transactions_info_to_json(self, transactions_info: List[Tuple[int, int, int]]) -> json:
        transactions = []
        for transaction_row in transactions_info:
            transaction_id, account_id, transaction_sum = transaction_row
            account_dict = {
                self.KEYS_FOR_TRANSACTIONS_JSON[0]: transaction_id,
                self.KEYS_FOR_TRANSACTIONS_JSON[1]: account_id,
                self.KEYS_FOR_TRANSACTIONS_JSON[2]: transaction_sum
            }
            transactions.append(account_dict)

        return json.dumps(transactions, indent=3)

