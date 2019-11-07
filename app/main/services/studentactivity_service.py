# Service for Activity related tasks

from app.main.models.StudentActivity import StudentActivity

def add_activity(activity):
    newActivity = StudentActivity(activity)
    newActivity.insert()

def getActivitiesByUser(userName):
    return StudentActivity.getActivitiesByUser(userName)