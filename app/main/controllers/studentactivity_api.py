# APIs for student activity

from flask import Blueprint, request
from app.main.services import studentactivity_service

studentactivity_api = Blueprint('studentactivity_api', __name__)

@studentactivity_api.route('/add', methods = ['POST'])
def add_activity():
    requestData = request.get_json()
    studentactivity_service.add_activity(requestData)
