"""Lorem ipsum"""


import uuid
import sqlite3
import re


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def emailValidator(email):
    """Function that checks and validates an email address
    and stops execution of code if email is not valid"""
    if not (re.fullmatch(regex, email)):
        print("Invalid Email")
        exit()

class User:
    def __inti__(self, id=uuid.uuid4, userName="", email="", password="", accountType="user"):
        self.id = id
        self.userName = userName
        self.email = email
        self.password = password
        self.accountType = accountType
        self.conn = sqlite3.connect("mdl.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id TEXT, userName TEXT, email TEXT, password TEXT)")
        self.conn.commit()

    def addUser(self,id, userName, email, password):
        self.cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (id, userName, email, password))
        self.conn.commit()
        print("success")

if __name__ == "__main__":
    print("add user func, lets see")
    print("1 add user")
    choice = input("choice")
    if choice == '1':
        id = uuid.uuid4()
        userName = input("user name")
        email = input("email")
        password = input("password")
        User.addUser(id, userName, email, password)