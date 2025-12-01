from exception import InvalidAccountError, AuthenticationError


account_table = {
    12345: "abcd",
    12346: "abce"
}

users_table = {
    12345: ["pavan", "123@gmail.com", 300],
    12346: ["ravi", "ravi@gmail.com", 5000]
}

def login(account: int, password: str):
    if account not in account_table:
        raise InvalidAccountError("Account number not found. Please try again.")
    
    if password != account_table[account]:
        raise AuthenticationError("Incorrect password. Please check your credentials.")

    print(f" Welcome, {users_table[account][0]}! You have successfully logged into Codegnan ATM.")
    return True

