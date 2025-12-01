from database.databaseConnection import database_config, cursor

def create_tables(): 
    
    account_table = """
    CREATE TABLE IF NOT EXISTS ACCOUNTS (
        ACCOUNT_NO INT PRIMARY KEY,
        PASSWORD VARCHAR(30) NOT NULL
    );
    """

    users_table = """
    CREATE TABLE IF NOT EXISTS USERS (
        USER_ID INT AUTO_INCREMENT PRIMARY KEY,
        ACCOUNT_NUMBER INT NOT NULL,
        USERNAME VARCHAR(50) NOT NULL,
        EMAIL VARCHAR(50) NOT NULL UNIQUE,
        AMOUNT DECIMAL(10, 2) DEFAULT 0,
        FOREIGN KEY (ACCOUNT_NUMBER) REFERENCES ACCOUNTS(ACCOUNT_NO)
    );
    """

    transactions_table = """
    CREATE TABLE IF NOT EXISTS TRANSACTIONS (
        TRANSACTION_ID INT AUTO_INCREMENT PRIMARY KEY,
        ACCOUNT_NUMBER INT NOT NULL,
        TRANSACTION_TYPE VARCHAR(20) NOT NULL,
        AMOUNT DECIMAL(10, 2) NOT NULL,
        TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ACCOUNT_NUMBER) REFERENCES ACCOUNTS(ACCOUNT_NO)
    );
    """

    cursor.execute(account_table)
    cursor.execute(users_table)
    cursor.execute(transactions_table)
    database_config.commit()
    print("Tables created successfully!")
