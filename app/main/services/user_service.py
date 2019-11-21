#  Service file for User
# All the business logic for the user module is present here
from app.main.models.User import User
from app.main.services import studentactivity_service
from app import bcrypt
from flask import Flask, session

def add_user(data):
    for key in data["basicDetails"]:
        data[key]=data["basicDetails"][key]
    del data["basicDetails"]
    activity = {
        "skills":data["skills"],
        "companies":data["companies"],
        "activity_type":"Register",
        "created_by":data["email"]
    }
    del data["skills"]
    del data["companies"]
    studentactivity_service.add_activity(activity)
    data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    User.insert(data)

def get_user(email):
    return User.fetch(email)


def get_all_users():
    # if "user_email" in session:
        # print(session["user_email"])
    return User.fetch_all_users()

def authenticateUser(email, password):
    if(User.count_query({"email":email})==0):
        return 404
    elif(bcrypt.check_password_hash(User.fetch(email)["password"], password)):
        session["user_email"] = email
        return 200
    else:
        return 204

def get_interested_companies_count(email):
    return len(User.fetch(email)["companies"])

def get_registered_skills_count(email):
    return len(User.fetch(email)["skills"])



