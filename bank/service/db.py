import mysql.connector


class DB:

    def __init__(self, host, username, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

    def get_accounts(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM bank_account ")
        accounts_table = cursor.fetchall()

        return accounts_table

