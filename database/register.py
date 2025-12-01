from database.databaseConnection import database_config, cursor
from database.utility import checkAccountStatus

# creating registe class
class Register:
    def __init__(self):
        pass
    def register(self, account_no:int,password:str, username:str, email:str, deposite_amount:int):
        try:
            # check account is exists or not
            check_account_status = checkAccountStatus(account_no)
            if check_account_status:
                return "Account number already exists. Please try with a different account number."
            else:
                # insert user account details in accounts tables
                insert_account_query = "INSERT INTO ACCOUNTS(ACCOUNT_NO, PASSWORD) VALUES(%s, %s);"
                cursor.execute(insert_account_query, (account_no, password))
                # insert user details in users table
                insert_user_query = "INSERT INTO users(ACCOUNT_NUMBER, USERNAME, EMAIL, AMOUNT) VALUES(%s, %s, %s, %s);"
                cursor.execute(insert_user_query, (account_no, username, email, deposite_amount))
                # insert initial deposit transaction in transactions table
                insert_transaction_query = "INSERT INTO TRANSACTIONS(ACCOUNT_NUMBER, TRANSACTION_TYPE,AMOUNT) \
                                        VALUES(%s, %s, %s);"    
                cursor.execute(insert_transaction_query, (account_no, "Deposite",deposite_amount))
                database_config.commit() # committing to database
                return "Registration successful and login to run again."
        except Exception as e:
            return f"Something wrong in database/Register.register: {e}"