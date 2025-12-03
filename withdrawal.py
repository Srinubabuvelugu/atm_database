from database.withdraw import Withdraw

def withdraw(account: int, amount: int):
    # creating object for withdraw class
    try:
        withdraw_obj = Withdraw()
        return withdraw_obj.withdrawAmount(account_no=account, withdraw_amount=amount)
    except Exception as e:
        return f"Something wrong in atm/withdraw.withdraw: {e}"
    