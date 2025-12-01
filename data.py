
account_table = {
    12345: "abcd",
    12346: "abce"
}

users_table = {
    12345: ["pavan", "123@gmail.com", 300],
    12346: ["ravi", "ravi@gmail.com", 5000]
}

# Check if account exists
def tab(account):
    return account in account_table

# Get a value from users_table
def ta(account, index):
    return users_table[account][index] if account in users_table else None

# Update a value in users_table
def updt(account, value=None, index=0):
    if account in users_table:
        if value is not None:
            users_table[account][index] = value
        return users_table[account][index]
    return None

#mini statement
def ministatement(account:int):
    return "Development Under process..."
    
#logout function definition
def logout():
    print("User successfully logout")
    exit()


