"""Lorem ipsum"""


import uuid
import sqlite3


class User:
    def __inti__(self, id, email, user_name, password, accountType):
        self.id = uuid.uuid4()
        self.email = email
        self.user_name = user_name
        self.password = password
        self.accountType = accountType


    def addUser(self, id, email, user_name, password, accountType):
        pass