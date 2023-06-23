import sqlite3
import hashlib
import re
import getpass
from Models.item import Item
from Models.user import * 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

conn = sqlite3.connect("mdl.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, itemName TEXT, price REAL, quantity INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, userName TEXT, email TEXT, password TEXT)")


def emailValidator(email):
    """Checks and validates an email address to make sure it is in a valid format
    (i.e user@service_provider.com) and stops execution of code if email is not valid"""
    if not (re.fullmatch(regex, email)):
        print("Invalid Email")
        exit()

def userNameValidator(userName):
    """Checks if userName already exists int the
    database and prompts user to try a different one if userName exists"""
    userName = str(userName)
    cur.execute("SELECT userName from users WHERE userName=?", (userName,))
    exists = cur.fetchone()
    if exists:
        print("User Name already exists please try another one")
        exit()

def getResponse():
    """Function that gets response from user and performs an operation
    based on the response"""
    response = input("Continue with delete operation?  Y/N: ")
    if not response == "Y":
        print("Operation cancelled")
        exit()


if __name__ == '__main__':
    print('')
    print('-----------------------------------------------------')
    print('Welcome to MD Logistics (CLI Application)')
    print('-----------------------------------------------------')
    print('')
    
    while True:
        print('Please select an option')
        print('')
        print('1. Login')
        print('2. Register')

        choice = input('What operation do you want to perform: ')
        if choice == '1':
            User.addUser()
        elif choice == '2':
            User.loginUser()
        elif choice == '3':
            break
        # TODO: Complete the choices section with all methods