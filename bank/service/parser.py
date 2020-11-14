import json
from typing import Tuple


class Parser:
    KEYS_FOR_ACCOUNTS_JSON = ["accountId", "opened", "sum"]

    def parse_accounts_info_to_json(self, accounts_info: Tuple[int, int, int]) -> json:
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

