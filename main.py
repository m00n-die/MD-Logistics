import sqlite3
import hashlib
import re
import getpass
from Models.item import Item
from Models.user import *
import os.path


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

def setAdminPassword():
    """Sets and admin password and saves it in a file 
    so only admins can perform
    some exclusive operations"""
    path = './adminPass.txt'
    if not os.path.exists(path):
        passwordFile = open ('adminPass.txt', 'r+')
        adminPass = str(input("Enter an admin password. This cannot be changed!: "))
        encrytped = hashlib.md5(adminPass.encode())
        digest = encrytped.hexdigest()
        passwordFile.write(digest)
        passwordFile.close()

if __name__ == '__main__':
    print('')
    print('-----------------------------------------------------')
    print('Welcome to MD Logistics (CLI Application)')
    print('-----------------------------------------------------')
    print('')
    
    while True:
        print('')
        print('USER\'S PAGE')
        print('')
        print('Please select an option')
        print('')
        print('1. Register (Sign Up)')
        print('2. Log In')
        print('3. Delete a User')
        print('4. Change Password')
        print('5. Change Account Email')
        print('6. Move to Inventory Items Page')
        print('7. Exit Application')

        print("What operation do you want to perform?")
        choice = input('Enter the corresponding number for the operation: ')
        
        if choice == '1':
            User.addUser()
        
        elif choice == '2':
            User.loginUser()
            loginStatus = True
        
        elif choice == '3':
            file = open('adminPass.txt', 'r')
            correctPassword = file.readline()
            password = str(input("Enter Admin Password: "))
            passwordEncrypted = hashlib.md5(password.encode())
            if passwordEncrypted.hexdigest() == correctPassword:
                User.removeUser
                print("Operation Succesful")
            else:
                print('Incorrect Password')
                exit()
        
        elif choice == '4':
            if loginStatus == True:
                User.updateUserPassword()
            else:
                print("Please log in first")
        
        elif choice == '5':
            if loginStatus == True:
                User.updateUserEmail()
            else:
                print('Please log in first')
        
        elif choice == '6':
            while True:
                print('')
                print("INVENTORY ITEMS PAGE")
                print('')
                print('1. Add an Item')
                print('2. Delete an Item')
                print('3. Update Item Info')
                print('4. View All Items')
                print('5. Search for an Item')
                print('6. Exit Application')

                option = input("Enter the corresponding number for the operation: ")
                
                if option == '1':
                    Item.addItem()
                
                elif option == '2':
                    Item.deleteItem()
                
                elif option == '3':
                    Item.updateItem()
                
                elif option == '4':
                    Item.viewItems()
                
                elif option == '5':
                    Item.searchItem()
                
                elif option == '6':
                    break
            
        elif choice == '7':
            break  