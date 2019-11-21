# Model file for jobPOstings
# All the CRUD operations for User are present here

import datetime
from app.database import DB


class JobPostings(object):

    """Collection level database operations are defined here"""

    @staticmethod
    def insert(postingObj):
        postingObj['created_at'] = datetime.datetime.utcnow()
        if DB.count("jobPostings", {"jobId": postingObj['jobId']}) <= 0:
            DB.insert(collection='jobPostings', data=postingObj)


    @staticmethod
    def update(jobId, query):
        return DB.update("jobPostings", {"jobId":jobId}, query)

    @staticmethod
    def fetch(jobId):
        return DB.find_one("jobPostings", {"jobId": jobId})

    @staticmethod
    def fetch_by_company(companyName):
        return DB.find("jobPostings", {"company": companyName})

    @staticmethod
    def fetch_all_postings():
        return DB.find("jobPostings")

    @staticmethod
    def fetch_open_position_count(companyName):
        return DB.count("jobPostings", {"company": companyName})

    