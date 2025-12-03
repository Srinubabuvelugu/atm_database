from database.databaseConnection import database_config, cursor
from database.utility import checkAccountStatus, getAmountFromDB, setAmountInDB

# creating class for Transfer
class Transfer:
    def __init__(self):
        pass
    def transferAmount(self, from_account:int, to_account:int, transfer_amount:int):
        try:
            # check account is exists or not in accounts tables
            if checkAccountStatus(from_account) and checkAccountStatus(to_account):
                # get amount from database
                from_account_amount = getAmountFromDB(account_no=from_account)
                if from_account_amount >=transfer_amount:
                    # calculate new amount
                    from_account_updated_amount = from_account_amount - transfer_amount
                    # update in transaction table and users table
                    setAmountInDB(account_no=from_account, \
                                  amount=from_account_updated_amount, \
                                    transaction_type="WITHDRAW(Transfer)")
                    to_account_amount = getAmountFromDB(account_no=to_account)
                    to_account_updated_amount = to_account_amount + transfer_amount
                    setAmountInDB(account_no=to_account, \
                                  amount=to_account_updated_amount, \
                                    transaction_type="DEPOSITE(Transfer)")
                    return f"Tranfer successful and current balance is {from_account_updated_amount}"
                else:
                    return "Insufficient balance"
            else:
                return "Account does not exist"
        except Exception as e:
            return f"Something wrong in database/tranfer.Transfer: {e}"