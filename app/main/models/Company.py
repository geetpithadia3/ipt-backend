# Model file for User
# All the CRUD operations for User are present here

import datetime
from app.database import DB


class Company(object):

    """Collection level database operations are defined here"""

    @staticmethod
    def insert(companyObj):
        companyObj['created_at'] = datetime.datetime.utcnow()
        if DB.count("company", {"name": companyObj['name']}) <= 0:
            DB.insert(collection='company', data=companyObj)


    @staticmethod
    def update(companyName, query):
        return DB.update("company", {"name":companyName}, query)

    @staticmethod
    def fetch(name):
        return DB.find_one("company", {"name": name})

    @staticmethod
    def fetch_all_companies():
        return DB.find("company")

    @staticmethod
    def fetch_all_company_details():
        return DB.find("company", {}, {"name": 1, "summary": 1, "website": 1})
