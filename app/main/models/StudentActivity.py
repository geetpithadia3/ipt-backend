# Model for Activities of User to be tracked
import datetime
from app.database import DB
class StudentActivity(object):
    def __init__(self,activity):
        self.skills = activity["skills"]
        self.companies = activity["companies"]
        self.created_by = activity["created_by"]
        self.created_at = datetime.datetime.utcnow()

    def insert(self):    
        DB.insert(collection='studentactivity', data=self.json())