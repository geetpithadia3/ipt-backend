# Service for Activity related tasks

from app.main.models.StudentActivity import StudentActivity
from flask import session
from bson.json_util import dumps
import pymongo
from app.main.services import jobPostings_service

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
    trackingResult = {}
    try:
        if "user_email" in session:
            userEmail = session["user_email"]
            activities = StudentActivity.getActivitiesByUser(userEmail).sort("created_at",pymongo.ASCENDING)
            trackingResult["trackingData"] = []
            for activity in activities:
                data = {}
                data["timeStamp"]= activity["created_at"]
                companies = activity["companies"]
                for company in companies:
                    postings = list(jobPostings_service.get_postings_by_company_name([company]))
                    for posting in postings:
                        position = posting["position"]
                        totalSkills = posting["skillsRequired"]
                        userSkills = activity["skills"]
                        probability = findProbability(userSkills, totalSkills)
                        data[company+"-"+position]= probability
                trackingResult["trackingData"].append(data)
            return trackingResult
        else:
            raise Exception('Invalid Activity as request is malformed')
    except Exception as identifier:
        print(identifier)
        raise Exception('Invalid Activity')

def findProbability(userSkills, totalSkills):
    userSkillsCount = 0
    totalSkillsArray = totalSkills.split(",")
    for userSkill in userSkills:
        if userSkill in totalSkillsArray:
            userSkillsCount += 1
    probability = ((userSkillsCount)/len(totalSkillsArray)) * 100
    return probability

def getSkillsList():
    if "user_email" in session:
        userEmail = session["user_email"]
        return getLatestUserActivity(userEmail)["skills"]

def updateSkills(data):
    try:
        if "user_email" in session:
            userEmail = session["user_email"]
            newActivity = StudentActivity.emptyObject()
            newActivity.activity_type = "Update"
            newActivity.companies = getLatestUserActivity(userEmail)["companies"]
            newActivity.created_by = userEmail
            newActivity.skills = data["skillsList"]
            newActivity.insert()
            return getLatestUserActivity(userEmail)
        else:
            raise Exception('Invalid Activity')
    except Exception as identifier:
        raise Exception('Invalid Activity')
    

