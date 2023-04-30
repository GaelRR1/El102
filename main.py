import mysql.connector
from tkinter import *
from tkinter import ttk
import datetime

date = datetime.datetime.now()

# bank administrator options and close accounts unit test maybe UI

connection = mysql.connector.connect(
    user = "root", 
    database = "example", 
    password = "Megatro102030#")

scenario_deposit =["deposit"]
scenario_withdraw =["withdraw"]
scenario_transfer =["transfer"]
scenario_show =["show", "present"]
scenario_extra = ['extra']
scenario_close = ['close']
scenario_modify = ['modify', 'change']
scenario_create = ['create']


def revis(sc,answer):
  for wo in sc:
    if wo in answer:
        return True

def withdraw(amount,number):    

    cursoo = connection.cursor()    
    
    amount = int(amount)
    number = int(number)
    cursoo.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))   

    b_balance = cursoo.fetchall()        

    print("Your before balance is: "+ str(b_balance)+" .")      
  
    
    cursoo.execute("UPDATE bank_account SET balance = balance - %s  WHERE account_number = %s", (amount,number))

    
    cursoo.execute("SELECT balance FROM bank_account WHERE account_number = %s", (number,))
    b_balance = cursoo.fetchone()[0] 

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
  
def modify(acc):
    k = str(input("What do you want to modify name or pin"))
    so = connection.cursor()
    if 'name' in k:
        mm = input("What will be the new name? \n")
        so.execute("UPDATE bank_account SET owner_name = %s  WHERE account_number = %s", (mm,acc))
        so.execute("SELECT owner_name FROM bank_account WHERE account_number = %s", (acc,))
        e = so.fetchone()[0]
        print(f"This is the new name {e}")
    else: 
        mm = int(input("What will be the new pin? \n"))
        so.execute("UPDATE bank_account SET pin = %s  WHERE account_number = %s", (mm,number))
        so.execute("SELECT pin FROM bank_account WHERE account_number = %s", (acc,))
        e = so.fetchone()[0]
        print(f"This is the new pin {e}")

    connection.commit()


def close(own): 
    v = input("Are you sure to delete " + str(own)+ "y/n")
    if v == 'y':
        n = input("Completely sure it will be deleted forever?")
        if n == 'y':
            v = connection.cursor()
            v.execute("DELETE FROM bank_account WHERE account_number = %s", (own,))
            print("Deleted")
    else:
        print("\n Your desicion")
    connection.commit()

def show(own):
    sh = connection.cursor()
    if own == 13:
        print("Hello, your admin account was detected")
        sh.execute("SELECT * FROM bank_account")
        for a in sh:
            print(a)
    else:
        print("Hello, your account has a limited access to information only possesing their numbers")
        sh.execute("SELECT account_number FROM bank_account WHERE owner_name != %s", (own,))
        for a in sh:
            print(a[0])

def create():
   name = str(input("What is your name? \n"))
   pin = int(input("what will be your pin? \n"))
   balance = int(input("What is the balance for your account?\n "))

   cr = connection.cursor()
   cr.execute("INSERT INTO bank_account (owner_name, date_creation, pin, balance) VALUES(%s,%s,%s,%s)", (name,date,pin,balance))
   

   ch = connection.cursor()
   ch.execute("SELECT * FROM bank_account WHERE owner_name = %s", (name,))
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
    
    next = input("So, what do you want to do next deposit, whithdraw, transfer, show available accounts or extra account options? (write end to stop)\n \n \n")

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
        inp = input("Who will receive the money? (put the account number) ")
        idd = connection.cursor()
        idd.execute("SELECT account_number FROM bank_account")
        ccc = idd.fetchall()

        ck = 0
        for a in ccc:
            if inp in str(a[0]):
                ck = 1
                break

        if ck == 1:
            transfer(both, ac_number, inp)
        else:
            print("Invalid account number. Please try again.")
    elif next == "end":
       print("Thank you for the time.")
       m += 1

    elif revis(scenario_extra, next):
       print("All of the options in here depend on your account.")

       if ac_number == 13:
            ex = input("Hello you want to close an account , modify one, or create one")
            if revis(scenario_modify,ex):
                ll = input("What will be the account number? ")
                modify(ll)

            elif revis(scenario_close,ex):
                ll = input("What will be the account number? ")
                close(ll)

            elif revis(scenario_create,ex):
                create()

            elif next == "end":
                print("Thank you for the time.")
                m += 1
       else:
            yx = input("Hello you can close your account or modify it")
            if revis(scenario_modify,ex):
                modify(ac_number)
            elif revis(scenario_close,ex):
                close(ac_number)
            elif next == "end":
                print("Thank you for the time.")
                m += 1    

       
       
cursorr.close()

connection.close()