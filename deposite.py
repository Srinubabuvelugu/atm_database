from database.deposite import Deposite
def deposite(account:int,amount:int):
    try:
        # creating object for deposite class
        deposite_obj = Deposite()
        return deposite_obj.depositeAmount(account_no=account, deposite_amount=amount)
    except Exception as e:
        return f"Something wrong in atm/deposite.deposite: {e}"    
    