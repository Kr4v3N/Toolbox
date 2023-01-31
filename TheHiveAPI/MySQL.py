import mysql.connector
import sys
import pprint

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password"
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute("SELECT User, Host FROM mysql.user;")

for entry in mycursor:
    print(entry)

mycursor.execute("SHOW DATABASES;")

for entry in mycursor:
    print(entry)