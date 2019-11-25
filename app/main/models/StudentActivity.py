# Model for Activities of User to be tracked
import datetime
from app.database import DB
class StudentActivity(object):
    def __init__(self,activity):
        self.skills = activity["skills"]
        self.companies = activity["companies"]
        self.created_by = activity["created_by"]
        self.activity_type = activity["activity_type"]
        self.created_at = datetime.datetime.utcnow()
    
    @classmethod
    def emptyObject(cls):
        obj = {}
        obj["skills"] = []
        obj["companies"] = []
        obj["created_by"] = ""
        obj["activity_type"] = ""
        obj["created_at"] = datetime.datetime.utcnow()
        return cls(obj)

    def json(self):
        return {
            'skills': self.skills,
            'companies': self.companies,
            'created_by': self.created_by,
            'created_at': self.created_at,
            'activity_type':self.activity_type
        }
    
    @staticmethod
    def getActivitiesByUser(userName):
        return DB.find("studentactivity", {"created_by": userName})

    @staticmethod
    def fetch(created_by):
        return DB.find("studentactivity", {"created_by": created_by})

    def insert(self):    
        DB.insert(collection='studentactivity', data=self.json())