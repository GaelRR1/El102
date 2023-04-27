import mysql.connector
from tkinter import *
from tkinter import ttk
import datetime

date = datetime.datetime.now()


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

    cursoo = connection.cursor()    
    
    amount = int(amount)
    number = int(number)
    cursoo.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))   

    b_balance = curso.fetchall()        

    print("Your before balance is: "+ str(b_balance)+" .")      
  
    
    cursoo.execute("UPDATE bank_account SET balance = balance - %s  WHERE account_number = %s", (amount,number))

    
    cursoo.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))
    b_balance = curso.fetchone()[0] 

    print("Your after balance is: "+str(b_balance)+" .")
    connection.commit()
 
def deposit(amount,number):    

    curso = connection.cursor()    
    
    amount = int(amount)
    number = int(number)
    curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))   

    b_balance = curso.fetchone()[0]        

    print("Your before balance is: "+ str(b_balance)+" .")      
  
    
    curso.execute("UPDATE bank_account SET balance = balance + %s  WHERE account_number = %s", (amount,number))

    
    curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))
    b_balance = curso.fetchone()[0] 

    print("Your after balance is: "+str(b_balance)+" .")
    connection.commit()
   
def transfer(amount,tnumber,Rnumber):
   #combine a deposit and whitdrwa function
   #take money
   print("\nStart to take money from "+str(tnumber)+"\n")
   withdraw(amount,tnumber)
   
   print("\nStart the deposit on "+str(Rnumber)+"\n")
   deposit(amount,Rnumber )
  


def show(own):
    sh = connection.cursor()
    if own == 13:
        sh.execute("SELECT * FROM bank_account")
        for a in sh:
            print(a)
    else:
        sh.execute("SELECT account_number FROM bank_account WHERE owner_name != %s", (own,))
        for a in sh:
            print(a[0])

def create():
   name = input("What is your name? \n")
   pin = input("what will be your pin? \n")
   balance = input("What is the balance for your account?\n ")

   cr = connection.cursor()
   cr.execute("INSERT INTO bank_account (owner_name, date_creation, pin, balance) VALUES(%s,%s,%s,%s)", (name,date,pin,balance))

   ch = connection.cursor()
   ch.execute("SELECT * FROM bank_account WHERE owner_name == %s", (name))
   aas= ch.fetchall()
   print(aas)
   connection.commit()
#---------------------------------------------------------------------------------------start run
cursorr = connection.cursor()
cursorr.execute("SELECT account_number, pin FROM bank_account")
ids = cursorr.fetchall() 
irt = 0
while irt == 0:
    quest = input("Do you posses an account? y/n")
    if quest == 'y':
        number = int(input("What is the account number? \n"))
        pin = int(input("what is the pin? \n"))

        x = tuple([number, pin])

        for acc in ids:
            if str(x) == str(acc):
                print("Your account is this "+str(acc))
                vali = input("Y/n? ")
                if vali == 'Y':
                    
                    nm = connection.cursor()
                    nm.execute("SELECT * From bank_account WHERE account_number = %s", (number,))
                    namee = nm.fetchone()[0]
                    full = nm.fetchall()
                    nm.close()
                    none = connection.cursor()
                    none.execute("SELECT account_number From bank_account WHERE account_number = %s", (number,))
                    ac_number = none.fetchone()[0]
                    none.close()
                    irt += 2
                else:
                    irt == 0
    else:
       create()

m = 0            
print(f"Hello {namee} welcome to GR Corporated. \n First here is your account {full}")
while m == 0:
    
    next = input("So, what do you want to do next deposit, whithdraw, transfer, or show available accounts? \n \n \n")

    if revis(scenario_deposit,next):
       ff = input("\nHow much you want to deposit? ")
       deposit(ff,ac_number)
    elif revis(scenario_withdraw,next):
       dd = input("\nHow much you want to take out? ")
       withdraw(dd,ac_number)
    elif revis(scenario_show,next):
       show(ac_number)
    elif revis(scenario_transfer,next):
       both = int(input("What will be the amount to transfer? \n"))
       ck = 0
       while ck == 0:
        inp = input("Who will recieve the money? ")
        idd = connection.cursor()
        idd.execute("SELECT acccount_number FROM bank_account")
        for a in idd:
           if inp == a:
              ck = 1
       transfer(both,ac_number,inp)
    elif next == "end":
       print("Thank you for the time.")
       continue
       
cursorr.close()

connection.close()