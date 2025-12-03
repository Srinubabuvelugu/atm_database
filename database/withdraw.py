from database.databaseConnection import database_config, cursor
from database.utility import checkAccountStatus, getAmountFromDB, setAmountInDB

# creating class for withdraw
class Withdraw:
    def __init__(self):
        pass
    def withdrawAmount(self, account_no:int, withdraw_amount:int):
        try:
            # check account is exists or not in accounts tables
            if checkAccountStatus(account_no=account_no):
                # get amount from database
                current_amount = getAmountFromDB(account_no=account_no)
                if current_amount >=withdraw_amount:
                    # calculate new amount
                    updated_amount = current_amount - withdraw_amount
                    # update in transaction table and users table
                    setAmountInDB(account_no=account_no, \
                                  amount=updated_amount, transaction_type="WITHDRAW")
                    return f"Withdraw successful and current balance is {updated_amount}"
                else:
                    return "Insufficient balance"
            else:
                return "Account does not exist"
        except Exception as e:
            return f"Something wrong in database/withdraw.withdrawAmount: {e}"