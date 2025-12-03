from database.databaseConnection import cursor, database_config
# checking account stsatus
def checkAccountStatus(account_no:int):
    try:
        # check account is exists or not
        check_account_query = "SELECT 1 FROM ACCOUNTS WHERE ACCOUNT_NO = %s;"
        cursor.execute(check_account_query, (account_no,))
        check_account_status = cursor.fetchall()
        if check_account_status:
            return True
        else:
            return False
        
    except Exception as e: 
        return f"Something wrong in database/utility.checkAccountStatus: {e}"
    
#creating function for get amount from database
def getAmountFromDB(account_no:int):
    try:
        get_amount_query= """SELECT AMOUNT FROM USERS 
                        WHERE ACCOUNT_NUMBER = %s;"""
        cursor.execute(get_amount_query,(account_no,))
        current_amount = cursor.fetchone()[0]
        return current_amount
    except Exception as e:
        return f"Something wrong in database/utility.getAmountFromDB: {e}"
    
# updating amount in database
def setAmountInDB(account_no:int, amount:int, transaction_type:str=None):
    try:
        update_amount_query = """UPDATE USERS SET AMOUNT = %s 
                                WHERE ACCOUNT_NUMBER = %s;"""
        cursor.execute(update_amount_query, (amount, account_no))
        # updating transaction table
        if transaction_type:
            insert_transaction_query = """INSERT INTO TRANSACTIONS
                                        (ACCOUNT_NUMBER, TRANSACTION_TYPE, AMOUNT)
                                        VALUES (%s, %s, %s);"""
            cursor.execute(insert_transaction_query, (account_no, transaction_type, amount))
        database_config.commit()
    except Exception as e:
        return f"Something wrong in database/utility.setAmountInDB: {e}"