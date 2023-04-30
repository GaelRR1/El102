import unittest
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
        so.execute("UPDATE bank_account SET pin = %s  WHERE account_number = %s", (mm,acc))
        so.execute("SELECT pin FROM bank_account WHERE account_number = %s", (acc,))
        e = so.fetchone()[0]
        print(f"This is the new pin {e}")



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

class TestBankFunctions(unittest.TestCase):
    
    def test_deposit(self):
        deposit(500, 13)
        curso = connection.cursor()
        curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (13,))
        b_balance = curso.fetchone()[0]
        self.assertEqual(b_balance, 1500)
    
    def test_withdraw(self):
        withdraw(500, 13)
        curso = connection.cursor()
        curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (13,))
        b_balance = curso.fetchone()[0]
        self.assertEqual(b_balance, 1000)
    
    def test_transfer(self):
        transfer(500, 13, 18)
        curso = connection.cursor()
        curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (13,))
        b_balance = curso.fetchone()[0]
        self.assertEqual(b_balance, 500)
        curso.execute("SELECT balance FROM bank_account WHERE account_number = %s", (18,))
        r_balance = curso.fetchone()[0]
        self.assertEqual(r_balance, 1500)
    
    def test_modify_name(self):
        modify(13, 'name')
        curso = connection.cursor()
        curso.execute("SELECT owner_name FROM bank_account WHERE account_number = %s", (13,))
        new_name = curso.fetchone()[0]
        self.assertEqual(new_name, 'John Smith')
    
    def test_modify_pin(self):
        modify(13, 'pin')
        curso = connection.cursor()
        curso.execute("SELECT pin FROM bank_account WHERE account_number = %s", (13,))
        new_pin = curso.fetchone()[0]
        self.assertEqual(new_pin, 1234)
    
    def test_close_account(self):
        close(13)
        curso = connection.cursor()
        curso.execute("SELECT * FROM bank_account WHERE account_number = %s", (13,))
        result = curso.fetchone()
        self.assertIsNone(result)
    
    def test_show_all_accounts(self):
        show(13)
        curso = connection.cursor()
        curso.execute("SELECT COUNT(*) FROM bank_account")
        num_accounts = curso.fetchone()[0]
        self.assertGreater(num_accounts, 0)
    
    def test_show_other_accounts(self):
        show(18)
        curso = connection.cursor()
        curso.execute("SELECT COUNT(*) FROM bank_account WHERE owner_name != %s", (18,))
        num_accounts = curso.fetchone()[0]
        self.assertGreater(num_accounts, 0)
    
    def test_create_account(self):
        create('Alice Brown', 4321, 1000)
        curso = connection.cursor()
        curso.execute("SELECT * FROM bank_account WHERE owner_name = %s", ('Alice Brown',))
        result = curso.fetchone()
        self.assertIsNotNone(result)
    
if __name__ == '__main__':
    unittest.main()