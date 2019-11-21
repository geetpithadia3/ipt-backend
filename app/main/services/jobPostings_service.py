#  Service file for Company
# All the business logic for the user module is present here
from app.main.models.JobPostings import JobPostings
from app import bcrypt
from flask import session
from app.main.services import studentactivity_service


def add_posting(data):
    JobPostings.insert(data)

def update_posting(data):
    JobPostings.update(jobId, data)

def get_posting(jobId):
    return JobPostings.fetch(jobId)

def get_postings():
    return JobPostings.fetch_all_postings()

def get_postings_by_company_name(companyName):
    return JobPostings.fetch_by_company(companyName)

def get_open_position_count():
    email=""
    if "user_email" in session:
        email = session["user_email"]
    print(email)
    activityObj=studentactivity_service.getLatestUserActivity(email)
    print(activityObj)
    count=0
    for company in activityObj["companies"]:
        count += JobPostings.fetch_open_position_count(company)
    return count

def get_skills_count():
    email=""
    if "user_email" in session:
        email = session["user_email"]
    print(email)
    activityObj=studentactivity_service.getLatestUserActivity(email)
    skillsDict={}
    for jobPosting in JobPostings.fetch_by_company(activityObj["companies"]):
        skills = jobPosting['skillsRequired'].split(',')
        for skill in skills:
            if skill.strip() in skillsDict:
                skillsDict[skill.strip()].append(jobPosting['company'])
            else:
                skillsDict[skill.strip()] = [jobPosting['company']]
            
    for key,value in skillsDict.items():
        skillsDict[key]=len(set(skillsDict[key]))  
    return skillsDict
    

