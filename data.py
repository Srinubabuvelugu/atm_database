from database.ministatement import Ministatement

#mini statement
def ministatement(account:int):
    ministatement_obj = Ministatement()
    transactions = ministatement_obj.get_ministatement(account_no=account)
    if type(transactions) == list:
        print("----------Ministatement----------")
        for trans in transactions:
            print(f"Transactions ID:{trans[0]} - Date:{trans[4]} \
                  - Type:{trans[2]} - Amount:{trans[3]}")
    else:
        print(transactions)
    return True

                                                       
    
#logout function definition
def logout():
    print("User successfully logout")
    exit()


