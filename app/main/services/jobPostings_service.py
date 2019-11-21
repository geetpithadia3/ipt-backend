#  Service file for Company
# All the business logic for the user module is present here
from app.main.models.JobPostings import JobPostings
from app import bcrypt


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

def get_open_position_count(companyList):
    count=0
    for company in companyList:
        count += JobPostings.fetch_open_position_count(company['companyName'])
    return count

def get_skills_count():
    skillsDict={}
    for jobPosting in JobPostings.fetch_all_postings():
        skills = jobPosting['skillsRequired'].split(',')
        for skill in skills:
            if skill.strip() in skillsDict:
                skillsDict[skill.strip()].append(jobPosting['company'])
            else:
                skillsDict[skill.strip()] = [jobPosting['company']]
            
    for key,value in skillsDict.items():
        skillsDict[key]=len(set(skillsDict[key]))  
    return skillsDict
    

