import mysql.connector
from mysql.connector import Error

# Establishing the connection
database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rhs@11341Willow',
)

# Creating a cursor object
cursorObj = database.cursor()

# selecting database
try:
    cursorObj.execute("USE crmdb")
    print("Database crmdb selected")
except Error as e:
    print("Error while connecting to MySQL", e.message)

