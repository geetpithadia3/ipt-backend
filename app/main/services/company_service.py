#  Service file for Company
# All the business logic for the user module is present here
from app.main.models.Company import Company
from app import bcrypt


def add_company(data):
    Company.insert(data)

def update_company(data):
    Company.update(name, data)

def get_compnay(name):
    Company.fetch(email)


def get_company_list():
    return Company.fetch_all_companies()


def get_company_details_list():
    return Company.fetch_all_company_details()


