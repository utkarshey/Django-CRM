# install MySQL on your local system - done
# pip install mysql
# pip install mysql-connector-python


# ----------------------------------------------------------------
import mysql.connector

# create a database connection
dataBase = mysql.connector.connect(
    host='localhost', 
    user='root', 
    passwd='root',
)

# prepare cursor object
cursorObject = dataBase.cursor("CREATE DATABASE elderco")
print("All done!")