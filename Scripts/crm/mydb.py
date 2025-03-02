import mysql.connector
from mysql.connector import Error 

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rhs@11341Willow'
    )


# prepare a cursor object
cursorObj = database.cursor()

# create a database
try:
    cursorObj.execute("USE crmdb")
    print('Done!!')
except Error as e:
    print(f"an error occurred: {e.msg}")    