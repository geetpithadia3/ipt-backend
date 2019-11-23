# Service for Activity related tasks

from app.main.models.StudentActivity import StudentActivity
from flask import session
from bson.json_util import dumps
import pymongo

def add_activity(activity):
    if "user_email" in session and session["user_email"] == activity["created_by"]:
        activity["activity_type"] = "Update"
    try:
        if activity["activity_type"] == "Register" or ("user_email" in session and session["user_email"] == activity["created_by"]):
            newActivity = StudentActivity(activity)
            newActivity.insert()
        else:
            raise Exception('Invalid Activity')
    except Exception as identifier:
        raise Exception('Invalid Activity')
    

def getActivitiesByUser(userName):
    return StudentActivity.getActivitiesByUser(userName)

def getLatestUserActivity(email):
    return StudentActivity.fetch(email).sort([("created_at",pymongo.DESCENDING)]).limit(1)[0]
    
def get_skills_companies_count():
    if "user_email" in session:
        email = session["user_email"]
    return {
        "company_count":len(StudentActivity.fetch(email).sort([("created_at",pymongo.DESCENDING)]).limit(1)[0]["companies"]),
        "skills_count":len(StudentActivity.fetch(email).sort([("created_at",pymongo.DESCENDING)]).limit(1)[0]["skills"])
    }

def trackUser():
    try:
        if "user_email" in session:
            userEmail = session["user_email"]
            activities = StudentActivity.getActivitiesByUser(userEmail)
            print(activities)
        else:
            raise Exception('Invalid Activity as request is malformed')
    except Exception as identifier:
        raise Exception('Invalid Activity')

