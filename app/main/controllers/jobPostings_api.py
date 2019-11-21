# API endpoint file for User

from flask import Blueprint, request
from bson.json_util import dumps
from app.main.services import jobPostings_service
from flask_cors import CORS, cross_origin

jobPostings_api = Blueprint('jobPostings_api', __name__)

"""API endpoints for JobPostings"""


@jobPostings_api.route('/add_posting', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_posting():
    requestData = request.get_json()
    jobPostings_service.add_posting(requestData)
    return dumps({'success': True}), 200, {'ContentType': 'application/json'}


@jobPostings_api.route('/get_postings_by_company_name/<companyName>')
@cross_origin(supports_credentials=True)
def get_postings_by_company_name(companyName):
    return dumps(jobPostings_service.get_postings_by_company_name(companyName))


@jobPostings_api.route('/get_postings')
@cross_origin(supports_credentials=True)
def get_postings():
    return dumps(jobPostings_service.get_postings())

@jobPostings_api.route('/get_posting/<jobId>')
@cross_origin(supports_credentials=True)
def get_posting():
    try:
        return jobPostings_service.get_posting(request.args.get())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@jobPostings_api.route('/get_open_position_count')
@cross_origin(supports_credentials=True)
def get_open_position_count():
    try:
        requestData = request.get_json()
        return dumps(jobPostings_service.get_open_position_count(requestData['companyList']))
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

