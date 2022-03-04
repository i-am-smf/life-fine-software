from tkinter import *
import mysql.connector

#connect to mysql
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="smfsql123",
    #database="LIFEFINE"
)

my_cursor=mydb.cursor()

my_cursor.execute("CREATE DATABASE LIFEFINE")
my_cursor.execute("CREATE DATABASE LIFEFINE_CUSTOMERS")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
