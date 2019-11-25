from flask import Blueprint, request, Response
from bson.json_util import dumps
from app.main.services import jobPostings_service,user_service, studentactivity_service
from flask_cors import CORS, cross_origin

dashboard_api = Blueprint('dashboard_api', __name__)

@dashboard_api.route('/get_open_position_count')
@cross_origin(supports_credentials=True)
def get_open_position_count():
    try:
        return dumps(jobPostings_service.get_open_position_count())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@dashboard_api.route('/get_skills_required_count')
@cross_origin(supports_credentials=True)
def get_skills_count():
    try:
        return dumps(jobPostings_service.get_skills_count())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@dashboard_api.route('/get_skills_companies_count')
@cross_origin(supports_credentials=True)
def get_companies_count():
    try:
        return dumps(studentactivity_service.get_skills_companies_count())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@dashboard_api.route('/get_relevant_job_postings')
@cross_origin(supports_credentials=True)
def get_relevant_job_postings():
    try:
        return dumps(jobPostings_service.get_relevant_job_postings())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@dashboard_api.route('/getskillslist')
@cross_origin(supports_credentials=True)
def getSkillsList():
    try:
        return dumps(studentactivity_service.getSkillsList())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')


@dashboard_api.route('/updateskillslist', methods = ['POST'])
@cross_origin(supports_credentials=True)
def updateSkills():
    try:
        requestData = request.get_json()
        return dumps({'success': True, 'data': studentactivity_service.updateSkills(requestData)})
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')
