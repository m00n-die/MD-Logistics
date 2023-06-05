import sqlite3
import hashlib
import re
import getpass


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

conn = sqlite3.connect("mdl.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, item_name TEXT, price REAL, item_qty INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT)")


def email_check(email):
    """Function that checks and validates an email address
    and stops execution of code if email is not valid"""
    if not (re.fullmatch(regex, email)):
        print("Invalid Email")
        exit()

def add_user():
    """Function that adds a new user to the users table"""
    email = input("Enter your email: ")
    email_check(email)
    email_hash = hashlib.md5(email.encode())
    #print(email_hash.hexdigest())
    email_digest = email_hash.hexdigest()
    cur.execute("SELECT email FROM users WHERE email=?", (email_digest,))
    exists = cur.fetchone()
    if exists:
        print("An account already exists with this email. Please log in or change your email.")
        exit()
    else:
        password = getpass.getpass(prompt="Enter a password: ")
        pass_hash = hashlib.md5(password.encode())
        #print(pass_hash.hexdigest())
        confirm = getpass.getpass(prompt="Confirm your password: ")
        confirm_hash = hashlib.md5(confirm.encode())
        #print(confirm_hash.hexdigest())
        if confirm_hash.hexdigest() == pass_hash.hexdigest():
            print("Account Creation Succesful")
            key = confirm_hash
            #print(key.hexdigest())
            key_digest = key.hexdigest()
        else:
            print("Password mismatch")
        cur.execute("INSERT INTO users VALUES (NULL, ?, ?)", (email_digest, key_digest))
        conn.commit()

def login_user():
    """Function that logs in an already existing user"""
    email = input("Enter your email: ")
    email_hash = hashlib.md5(email.encode())
    email_digest = email_hash.hexdigest()
    cur.execute("SELECT email FROM users WHERE email=?", (email_digest,))
    exists = cur.fetchone()
    if exists:
        password = getpass.getpass(prompt="Enter your password: ")
        password_hash = hashlib.md5(password.encode())
        #print(password_hash.hexdigest())
        cur.execute("SELECT password FROM users WHERE email=?", (email_digest,))
        valid_key = cur.fetchone()
        #print(valid_key)
        key = ('{}'.format(password_hash.hexdigest()),)
        #print(key)
        if key == valid_key:
            # fetchone() returns a tuple, so this is done to get the real value alone.
            print("Login Success")
        else:
            print("Incorrect password. Try again.")
            exit()
    else:
        print("Your email is not registered with an account. Please register")
        exit()

def add_item():
    """Function that adds an item to the inventory table"""
    name = input("Name of item: ")
    price = input("Price of {}: ".format(name))
    qty = input("Quantity of {}: ".format(name))
    cur.exectute("INSERT INTO inventory VALUES (NULL, ?, ?, ?)", (name, price, qty))
    

#add_user()
#login_user()