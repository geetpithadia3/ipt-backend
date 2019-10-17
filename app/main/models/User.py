import datetime

from app.database import DB


class User(object):

    """Collection level database operations are defined here"""

    def __init__(self, name):
        self.name = name
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        if not DB.find_one("users", {"name": self.name}):
            DB.insert(collection='users', data=self.json())

    @staticmethod
    def fetch(name):
        return DB.find_one("users", {"name": name})

    @staticmethod
    def fetch_all_users():
        return DB.find("users")

    def json(self):
        return {
            'name': self.name,
            'created_at': self.created_at
        }
