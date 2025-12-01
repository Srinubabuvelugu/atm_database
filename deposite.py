import data as d
#deposite function definition
def deposite(account:int,amount:int):
    if  d.tab(account):
        c=d.updt(account=account,index=2)+amount
        b=d.updt(account=account,value=c,index=2)

        return f"{amount} Deposite successful and current balance is {b}"
    else:
        return "User not found"