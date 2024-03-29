"""A User class that represtnts all users of the application
The class has common attributes of all users"""

import hashlib
import getpass
import sqlite3
from main import userNameValidator
from main import emailValidator
from main import getResponse

conn = sqlite3.connect("mdl.db")
cur = conn.cursor()

class User:
    """Lorem ipsum"""
    def __init__(self, userName, email, password):
        """Initializes the class with userName, email and password"""
        self.userName = userName
        self.email = email
        self.password = password

    def addUser():
        """Creates a new user and adds the user to the database"""
        userName = input("Please enter your User Name: ")
        userNameValidator(userName)
        email = input("Enter your email: ")
        emailValidator(email)
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
                # print(pass_hash.hexdigest())
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
        cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (userName, email_digest, key_digest))
        conn.commit()
        
    def loginUser():
        """Logs in a user with their user name and password"""
        userName = input("Enter your user name: ")
        #email = input("Enter your email: ")
        #email_hash = hashlib.md5(email.encode())
        #email_digest = email_hash.hexdigest()
        cur.execute("SELECT userName FROM users WHERE userName=?", (userName,))
        exists = cur.fetchone()
        if exists:
            password = getpass.getpass(prompt="Enter your password: ")
            password_hash = hashlib.md5(password.encode())
            #print(password_hash.hexdigest())
            cur.execute("SELECT password FROM users WHERE userName=?", (userName,))
            validKey = cur.fetchone()
            #print(valid_key)
            key = ('{}'.format(password_hash.hexdigest()),)
            #print(key)
            if key == validKey:
                # fetchone() returns a tuple, so this is done to get the real value alone.
                print("Login Success")
                User.loginStatus = True
            else:
                print("Incorrect password. Try again.")
                exit() 
        else:
            print("No account is registered with user name. Please register")
            exit()
    conn.commit()

    def removeUser():
        """Function that removes or deletes a user from the database"""
        userName = input("Enter the user name of the account to be deleted: ")
        cur.execute("SELECT userName FROM users WHERE userName=?", (userName,))
        exists = cur.fetchone()
        if exists:
            print("Are you sure you want to delete user '{}'? This action cannot be undone!".format(userName))
            getResponse()
            cur.execute("DELETE FROM users WHERE userName=?", (userName,))
            print("User: '{}' deleted".format(userName))
        else:
            print("There is no account registered with username: {}".format(userName))
            exit()
        conn.commit()

    def updateUserPassword():
        """Function that updates the information or data on a user"""
        print("Please login again with your old password.")
        print("")
        User.loginUser()
        if User.loginStatus == True:
            email = input("Enter your account email: ")
            emailValidator(email)
            emailHash = hashlib.md5(email.encode())
            emailDigest = emailHash.hexdigest()
            cur.execute("SELECT email FROM users WHERE email=?", (emailDigest,))
            exists = cur.fetchone()
            if exists:
                newPassword = getpass.getpass(prompt="Enter your new password: ")
                newPasswordHash = hashlib.md5(newPassword.encode())
                confirmPassword = getpass.getpass(prompt="Confirm password: ")
                confirmPasswordHash = hashlib.md5(confirmPassword.encode())
                if confirmPasswordHash.hexdigest() == newPasswordHash.hexdigest():
                    password = confirmPasswordHash.hexdigest()
                    cur.execute("UPDATE users SET password=? WHERE email=?", (password, emailDigest))
                    conn.commit()
                    print("Password successfully updated")
                else:
                    print("Password mismatch")
                    
        else:
            print("Login unsuccessful. Please try again")                

    def updateUserEmail():
        """Updates the email of a user. User must first be logged in to prform this action"""
        print("Please login")
        User.loginUser()  
        if User.loginstatus == True:
            oldEmail = input("Enter your old email: ")
            oldEmailHash = hashlib.md5(oldEmail.encode())
            oldEmailDigest = oldEmailHash.hexdigest()
            cur.execute("SELECT email FROM users WHERE email=?", (oldEmailDigest,))
            exists = cur.fetchone()
            if exists:
                newEmail = input("Enter your new email address: ")
                emailValidator(newEmail)
                newEmailHash = hashlib.md5(newEmail.encode())
                confirmEmail = input("Confirm new email: ")
                emailValidator(confirmEmail)
                confirmEmailHash = hashlib.md5(confirmEmail.encode())
                if confirmEmailHash.hexdigest() == newEmailHash.hexdigest():
                    email = confirmEmailHash.hexdigest()
                    cur.execute("UPDATE users SET email=? WHERE email=?", (email, oldEmailDigest))
                    conn.commit()
                    print("Email successfully updated")
                else:
                    print("Password mismatch")
        else:
            print("Login unsuccessful. Please try again")