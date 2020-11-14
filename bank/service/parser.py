import json
from typing import Tuple, List


class Parser:
    KEYS_FOR_ACCOUNTS_JSON = ["accountId", "opened", "sum"]
    KEYS_FOR_TRANSACTIONS_JSON = ["transactionId", "accountId", "sum"]

    def parse_list_info_to_json(self, entities_list:List[Tuple[int, int, int]], entity_type: str) -> json:
        entities = []
        for entity_row in entities_list:
            first_key, second_key, third_key = entity_row
            if entity_type == 'account':
                entity_dict = {
                    self.KEYS_FOR_ACCOUNTS_JSON[0]: first_key,
                    self.KEYS_FOR_ACCOUNTS_JSON[1]: second_key,
                    self.KEYS_FOR_ACCOUNTS_JSON[2]: third_key
                }
            else:
                entity_dict = {
                    self.KEYS_FOR_TRANSACTIONS_JSON[0]: first_key,
                    self.KEYS_FOR_TRANSACTIONS_JSON[1]: second_key,
                    self.KEYS_FOR_TRANSACTIONS_JSON[2]: third_key
                }
            entities.append(entity_dict)

        return json.dumps(entities, indent=3)

    def parse_account_item_info_to_json(self, account_row: List[Tuple[int, int, int]]) -> json:
        # list always contains one element
        account_id, opened, account_sum = account_row[0]
        account_dict = {
            self.KEYS_FOR_ACCOUNTS_JSON[0]: account_id,
            self.KEYS_FOR_ACCOUNTS_JSON[1]: opened,
            self.KEYS_FOR_ACCOUNTS_JSON[2]: account_sum
        }

        return json.dumps(account_dict, indent=3)
