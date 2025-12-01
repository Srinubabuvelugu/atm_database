import data as d
#Transfer function definition
def transfer(account:int,to_account:int,amount:int):
    if  d.tab(account=account):
        if  d.tab(account=to_account):
            curr_amount=d.ta(account=account,index=2)
            if curr_amount>=amount:
                c=d.updt(account=account,index=2)-amount
                b1=d.updt(account=account,value=c,index=2)
                b=d.updt(account=account,index=2)+amount
                e=d.updt(account=account,value=b,index=2)
                return f"{amount} Transfer successful current balance is {b1}"
            else:
                return "Insufficient amount"
        else:
            return "Reciever not found"
    else:
        return "User not found"