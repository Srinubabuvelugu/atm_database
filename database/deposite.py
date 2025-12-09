from database.databaseConnection import database_config, cursor
from database.utility import checkAccountStatus, getAmountFromDB, setAmountInDB

# creating class for withdraw
class Deposite:
    def __init__(self):
        pass
    def depositeAmount(self, account_no:int, deposite_amount:int):
        try:
            # check account is exists or not in accounts tables
            if checkAccountStatus(account_no=account_no):
                # get amount from database
                current_amount = getAmountFromDB(account_no=account_no)
                
                # calculate new amount
                updated_amount = current_amount + deposite_amount
                # update in transaction table and users table
                setAmountInDB(account_no=account_no, \
                              amount=deposite_amount, transaction_type="DEPOSITE")
                return f"Deposite successful and current balance is {updated_amount}"
                
            else:
                return "Account does not exist"
        except Exception as e:
            return f"Something wrong in database/deposite.Deposite.depositeAmount: {e}"