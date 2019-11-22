# API endpoint file for User

from flask import Blueprint, request
from bson.json_util import dumps
from app.main.services import company_service
from flask_cors import CORS, cross_origin

company_api = Blueprint('company_api', __name__)

"""API endpoints for Company"""


@company_api.route('/add_company', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_company():
    requestData = request.get_json()
    company_service.add_company(requestData)
    return dumps({'success': True}), 200, {'ContentType': 'application/json'}


@company_api.route('/get_company/<companyName>')
@cross_origin(supports_credentials=True)
def get_company():
    name = request.args.get()
    return company_service.add_company(name)


@company_api.route('/get_company_details_list')
@cross_origin(supports_credentials=True)
def get_company_details_list():
    try:
        return dumps(company_service.get_company_details_list())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@company_api.route('/get_company_list')
@cross_origin(supports_credentials=True)
def get_company_list():
    try:
        return dumps(company_service.get_company_list())
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')
        

