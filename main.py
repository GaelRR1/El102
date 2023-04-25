import mysql.connector
from tkinter import *
from tkinter import ttk

 

connection = mysql.connector.connect(
    user = "root", 
    database = "example", 
    password = "Megatro102030#")

 
cursorr = connection.cursor()
cursorr.execute("SELECT account_number, pin FROM bank_account")
ids = cursorr.fetchall() 
i=0
number = input("What is the account number? \n")
pin = input("what is the pin? \n")

x = tuple([number, pin])

for acc in ids:
    print(acc)
    if str(x) == str(acc):
        print("Your account is this "+str(acc))
        print(x)
            

cursorr.close()

connection.close()