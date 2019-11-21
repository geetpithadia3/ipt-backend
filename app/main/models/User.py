# Model file for User
# All the CRUD operations for User are present here

import datetime
from app.database import DB


class User(object):

    """Collection level database operations are defined here"""

    @staticmethod
    def insert(userObj):
        
        userObj['created_at'] = datetime.datetime.utcnow()
        if DB.count("users", {"email": userObj['email']})<=0:
            DB.insert(collection='users', data=userObj)

    @staticmethod
    def fetch(email):
        return DB.find_one("users", {"email": email})

    @staticmethod
    def fetch_all_users():
        return DB.find("users")
    
    
    @staticmethod
    def count_query(query):
        return DB.count("users", query)