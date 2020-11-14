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
        cursor.execute("SELECT * FROM BANK_ACCOUNT")
        db_response = cursor.fetchall()

        return db_response

    def get_account(self, account_id: int):
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM BANK_ACCOUNT WHERE ACCOUNT_ID = {account_id}")
        db_response = cursor.fetchall()

        return db_response

    def get_transactions(self, account_id: int):
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM TRANSACTION WHERE ACCOUNT_ID = {account_id}")
        db_response = cursor.fetchall()

        return db_response

    def put_money(self, account_id: int, sum: int):
        cursor = self.db.cursor()
        cursor.execute(f"UPDATE BANK_ACCOUNT SET `SUM` = `SUM` + {sum} WHERE ACCOUNT_ID = {account_id}")
        self.db.commit()
        print(cursor.rowcount, "record(s) affected")

        cursor = self.db.cursor()
        cursor.execute(f"INSERT INTO TRANSACTION (ACCOUNT_ID, SUM) VALUES ({account_id}, {sum})")
        self.db.commit()
        print(cursor.rowcount, "record inserted.")

