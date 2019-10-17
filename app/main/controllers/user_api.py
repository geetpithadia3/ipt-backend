from flask import Blueprint
from app.main.services import user_service
from bson.json_util import dumps

user_api = Blueprint('user_api', __name__)

"""API endpoints for USER"""
@user_api.route('/add_user')
def add_user():
    """need to pass the data"""
    user_service.add_user()


@user_api.route('/get_user')
def get_user(name):
    return user_service.get_user(name);


@user_api.route('/get_all_users')
def get_all_users():
    try:
        return user_service.get_all_users()
    except Exception as e:
        return dumps({'error': str(e)})

