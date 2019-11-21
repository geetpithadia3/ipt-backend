from flask import Blueprint, request, Response
from bson.json_util import dumps
from app.main.services import jobPostings_service,user_service
from flask_cors import CORS, cross_origin

dashboard_api = Blueprint('dashboard_api', __name__)

@dashboard_api.route('/get_open_position_count',methods=['POST'])
@cross_origin(supports_credentials=True)
def get_open_position_count():
    try:
        requestData = request.get_json()
        return dumps(jobPostings_service.get_open_position_count(requestData['companyList']))
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@dashboard_api.route('/get_skills_count')
@cross_origin(supports_credentials=True)
def get_skills_count():
    try:
        return dumps(jobPostings_service.get_skills_count())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@dashboard_api.route('/get_companies_count/<email>')
@cross_origin(supports_credentials=True)
def get_companies_count(email):
    try:
        return dumps(user_service.get_interested_companies_count(email))
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@dashboard_api.route('/get_registered_skills_count/<email>')
@cross_origin(supports_credentials=True)
def get_registered_skills_count(email):
    try:
        return dumps(user_service.get_registered_skills_count(email))
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')