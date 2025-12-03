from database.login import Login
def login(account: int, password: str):
    try:
        # creating object for Login class
        login_obj = Login()
        return login_obj.login(account_no=account, password=password)
    except Exception as e:
        return f"Something wrong in atm/login.login: {e}"   