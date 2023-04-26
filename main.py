import mysql.connector
from tkinter import *
from tkinter import ttk

 

connection = mysql.connector.connect(
    user = "root", 
    database = "example", 
    password = "Megatro102030#")

scenario_deposit =["deposit"]
scenario_withdraw =["withdraw"]
scenario_transfer =["transfer"]
scenario_show =["show", "present"]



def revis(sc,answer):
  for wo in sc:
    if wo in answer:
        return True

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
 
def deposit(amount,number):    

    curso = connection.cursor()    
    
    amount = int(amount)
    number = int(number)
    curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))   

    b_balance = curso.fetchall()        

    print("Your before balance is: "+ str(b_balance)+" .")      
  
    
    curso.execute("UPDATE bank_account SET balance = balance + %s  WHERE account_number = %s", (amount,number))

    
    curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))
    b_balance = curso.fetchone()[0] 

    print("Your after balance is: "+str(b_balance)+" .")
    connection.commit()
   
def show(own):
   sh = connection.cursor()
   sh.execute("Select * FROM bank_account WHERE owner_name != %s", (own,))
   print(account)
   for a in sh:
      print(" "+a+"\n")

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
    next = input("So, what do you want to do next deposit, whithdraw, transfer, or show available accounts? \n \n \n")

    if revis(scenario_deposit,next):
       deposit()
    elif revis(scenario_withdraw,next):
       withdraw()
    elif revis(scenario_show,next):
       show(name)
    elif revis(scenario_transfer,next):
       transfer()
       
cursorr.close()

connection.close()