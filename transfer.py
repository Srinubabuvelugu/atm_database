from database.transfer import Transfer
#Transfer function definition
def transfer(account:int,to_account:int,amount:int):
    try:
        # creating object for Transfer class
        transfer_obj = Transfer()
        return transfer_obj.transferAmount(from_account=account, \
                            to_account=to_account, transfer_amount=amount)
    except Exception as e:
        return f"Something wrong in atm/transfer.transfer: {e}"
    