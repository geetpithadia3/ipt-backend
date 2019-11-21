# Service for Activity related tasks

from app.main.models.StudentActivity import StudentActivity
from flask import session
from bson.json_util import dumps
import pymongo

def add_activity(activity):
    newActivity = StudentActivity(activity)
    newActivity.insert()

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


