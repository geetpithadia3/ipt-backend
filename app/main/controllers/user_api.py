# API endpoint file for User

from flask import Blueprint, request
from app.main.services import user_service
from bson.json_util import dumps
from flask_cors import CORS, cross_origin

user_api = Blueprint('user_api', __name__)

"""API endpoints for USER"""

@user_api.route('/add_user', methods = ['POST'])
@cross_origin(supports_credentials=True)
def add_user():
    requestData = request.get_json()
    user_service.add_user(requestData)
    return dumps({'success':True}), 200, {'ContentType':'application/json'} 


@user_api.route('/get_user')
def get_user(name):
    return user_service.get_user(name);

@user_api.route('/get_all_users')
def get_all_users():
    try:
        return user_service.get_all_users()
    except Exception as e:
        return dumps({'error': str(e)})


@user_api.route('/authenticate', methods = ['POST'])
def authenticateUser():
    try:
        requestData = request.get_json();
        return user_service.authenticateUser(requestData['username'],requestData['password'])
    except Exception as e:
        return dumps({'error': str(e)})

