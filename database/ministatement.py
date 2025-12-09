from database.databaseConnection import database_config, cursor

# creating class for ministatement
class Ministatement:
    def __init__(self):
        pass
    def get_ministatement(self, account_no:int):
        try:
            transactions_query = """SELECT * FROM TRANSACTIONS
                                WHERE ACCOUNT_NUMBER = %s
                                ORDER BY TIMESTAMP DESC
                                LIMIT 10;"""
            cursor.execute(transactions_query, (account_no,))
            transactions = cursor.fetchall()
            if transactions:
                return transactions
            else:
                return "No transaction found"
        except Exception as e:
            return f"Something wrong in database/ministatement.py:{e}"