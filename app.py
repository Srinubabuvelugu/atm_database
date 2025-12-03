import data as d
import balance as b
import deposite as dp
import withdrawal as w
import login as log
import transfer as t
from exception import *

# importing tables file
from database.tables import create_tables
from database.register import Register
from database.login import Login
#operations
operations=(
    "1. Balance enquiry \n",
    "2. Withdrawal \n",
    "3. Deposite \n",
    "4. Transfer \n",
    "5. Mini statement \n",
    "6. Logout"
)

#main
if __name__ == "__main__":
    print("Welcome to codegnan ATM")
    # calling crate_tables function to create tables if not exists
    create_tables()

    choice = int(input("1. Register \n2. Login \n Select your operation:"))
    if choice == 1:
        try:
            account_no = int(input("Please Enter your account number:"))
            password = input("Please Enter your password:")
            username = input("Please enter your username:")
            email = input("please enter your email:")
            deposite_amount = int(input("Please enter your initial deposite amount:"))
            register_obj = Register()
            register_status = register_obj.register(account_no=account_no,
                                                password = password,
                                                username = username,
                                                email = email,
                                                deposite_amount = deposite_amount)
            print(register_status)
        except Exception as e:
            print(f"Registration failed atm/app.py: {e}")
    elif choice == 2:
        try:

            account_no = int(input("Please enter your account number: "))
            password = input("Please enter Password: ")

            login_val = log.login(account=account_no, password=password)

            while login_val:
                print(*operations)
                try:
                    choice = int(input("Please select your operation: "))

                    if choice == 1:
                        print(b.balance(account=account_no))

                    elif choice == 2:
                        withdraw_amount = int(input("Enter withdraw amount: "))
                        print(w.withdraw(account=account_no, amount=withdraw_amount))

                    elif choice == 3:
                        deposit_amount = int(input("Enter deposit amount: "))
                        print(dp.deposite(account=account_no, amount=deposit_amount))

                    elif choice == 4:
                        receiver_acc = int(input("Enter receiver account number: "))
                        transfer_amount = int(input("Enter amount: "))
                        print(t.transfer(account=account_no, to_account=receiver_acc, amount=transfer_amount))

                    elif choice == 5:
                        print(d.ministatement(account=account_no))

                    elif choice == 6:
                        d.logout()
                        print("Logged out successfully.")
                        break

                    else:
                        print("Please select a valid operation.")

                except (InvalidAmountError, InsufficientBalanceError,
                        InvalidAccountError, AuthenticationError) as e:
                    print(f"Error: {e}")

                except ValueError:
                    print("Invalid input. Please enter numeric values only.")

        except InvalidAccountError as e:
            print(f"Login failed: {e}")
        except AuthenticationError as e:
            print(f"Login failed: {e}")
        except ValueError:
            print("Invalid input! Account number must be digits only.")


