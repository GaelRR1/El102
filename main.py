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
while i == 0 :
    number = int(input("What is the account number? \n"))
    pin = int(input("what is the pin? \n"))

    x = tuple([number, pin])

    for acc in ids:
        if str(x) == str(acc):
            print("Your account is this "+str(acc))
            vali = input("Y/n? ")
            if vali == 'Y':
                i += 2
            else:
                i == 0
                
cursorr.close()

connection.close()