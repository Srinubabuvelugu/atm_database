from database.databaseConnection import cursor
# checking account stsatus
def checkAccountStatus(account_no:int):
    try:
        # check account is exists or not
        check_account_query = "SELECT 1 FROM ACCOUNTS WHERE ACCOUNT_NO = %s;"
        cursor.execute(check_account_query, (account_no,))
        check_account_status = cursor.fetchall()
        return check_account_status
    except Exception as e: 
        return f"Something wrong in database/utility.checkAccountStatus: {e}"