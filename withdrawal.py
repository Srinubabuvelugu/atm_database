


import data as d
from exception import InvalidAccountError, InsufficientBalanceError, InvalidAmountError

def withdraw(account: int, amount: int):
    
    if not d.tab(account):
        raise InvalidAccountError("User not found. Please check account number.")

    if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be greater than zero.")

    curr_balance = d.updt(account=account, index=2)


    if curr_balance < amount:
        raise InsufficientBalanceError("Insufficient funds for this transaction.")

    
    new_balance = curr_balance - amount
    d.updt(account=account, value=new_balance, index=2)

    
   

    return f" Withdrawal successful! Current balance: {new_balance}"
