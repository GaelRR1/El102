import mysql.connector
from tkinter import *
from tkinter import ttk

 

connection = mysql.connector.connect(
    user = "root", 
    database = "example", 
    password = "Megatro102030#")

 
cursor = connection.cursor()


def initial_show(number):
    
## START -------------------------------------------------------------------------

    print("Hello, welcome to GR Corporated\nWe need to login enter your information. \n")
i = 0
cursorr = connection.cursor()
cursorr.execute("SELECT account_number, pin FROM bank_account")
ids = cursorr.fetchall() 
while i == 0 :
    number = input("What is the account number? \n")
    pin = input("what is the pin? \n")

    x = tuple([number, pin])
    print(x)

    for acc in ids:
        if str(x) == str(acc):
            print("Your account is this "+str(acc))
            vali = input("Y/n? ")
            if vali == 'Y':
                i == 2
            else:
                i == 0

cursor.close()

connection.close()