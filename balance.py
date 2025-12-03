from database.utility import getAmountFromDB, checkAccountStatus
def balance(account:int):
    try:
        if checkAccountStatus(account_no=account):
            curr_amount = getAmountFromDB(account_no=account)
            return f"Current balance is {curr_amount}"
        else:
            return "Account does not exist"
    except Exception as e:
        return f"Something wrong in database/balance.balance: {e}"
    