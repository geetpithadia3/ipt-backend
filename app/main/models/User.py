# Model file for User
# All the CRUD operations for User are present here

import datetime
from app.database import DB


class User(object):

    """Collection level database operations are defined here"""

    def __init__(self,userObj):
        self.username = userObj["username"]
        self.password = userObj["password"]
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        print(DB.count("users", {"username": self.username}))
        if DB.count("users", {"username": self.username})<=0:
            DB.insert(collection='users', data=self.json())

    @staticmethod
    def fetch(username):
        return DB.find_one("users", {"username": username})

    @staticmethod
    def fetch_all_users():
        return DB.find("users")

    def json(self):
        return {
            'username': self.username,
            'password': self.password,
            'created_at': self.created_at
        }
