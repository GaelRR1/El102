import mysql.connector
from tkinter import *
from tkinter import ttk

 

connection = mysql.connector.connect(
    user = "root", 
    database = "example", 
    password = "Megatro102030#")

def withdraw(amount,number):    
    curso = connection.cursor()    
    
    amount = int(amount)
    number = int(number)
    curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))   

    b_balance = curso.fetchall()        

    print("Your before balance is: "+ str(b_balance)+" .")      
  
    
    curso.execute("UPDATE bank_account SET balance = balance - %s  WHERE account_number = %s", (amount,number))

    
    curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))
    b_balance = curso.fetchone()[0] 

    print("Your after balance is: "+str(b_balance)+" .")
    connection.commit()
 
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
                nm = connection.cursor()
                nm.execute("SELECT * From bank_account")
                name = nm.fetchone()[0]
                account = nm.fetchall()
            else:
                i == 0

m = 0            
while m == 0:
    print(f"Hello {name} welcome to GR Corporated. \n First here is your account {account}")
    next = input("So, what do you want to do next deposit, whithdraw, transfer, or show available accounts? \n")
cursorr.close()

connection.close()