from database.databaseConnection import database_config, cursor
from database.utility import checkAccountStatus
# creating login class
class Login:
    def login(account_no:int, password:str):
        try:
            if checkAccountStatus(account_no= account_no):
                # get password from database
                password_query = "SELECT PASSWORD FROM ACCOUNTS WHERE ACCOUNT_NO = %s;"
                cursor.execute(password_query, (account_no,))
                dp_password = cursor.fetchone()[0]
                if dp_password == password:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return f"Something wrong in database/Login.login: {e}"