import mysql.connector as SQLC
# login to database
database_config = SQLC.connect(
    host = "localhost",
    user = "root",
    password = 'root',
    database = "bank"

)
# creating cursor object
cursor = database_config.cursor()
# print(cursor,database_config)