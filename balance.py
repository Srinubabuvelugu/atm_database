import data as d
def balance(account:int):
    if  d.tab(account):
        curr_amount=d.ta(account,2)
        return f"Current balance is {curr_amount}"
    else:
        return "User not found"