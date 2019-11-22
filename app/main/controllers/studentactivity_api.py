# APIs for student activity

from flask import Blueprint, request, Response
from app.main.services import studentactivity_service
from bson.json_util import dumps
from flask_cors import CORS, cross_origin

studentactivity_api = Blueprint('studentactivity_api', __name__)

@studentactivity_api.route('/add', methods = ['POST'])
@cross_origin(supports_credentials=True)
def add_activity():
    try:
        requestData = request.get_json()
        studentactivity_service.add_activity(requestData)
        return dumps({'success': True, 'data': studentactivity_service.getActivitiesByUser(requestData["created_by"])})
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')

@studentactivity_api.route('/getactivitesbyuser', methods = ['GET'])
@cross_origin(supports_credentials=True)
def getActivitiesByUser():
    try:
        username = request.args.get('username')
        return dumps({'success': True, 'data': studentactivity_service.getActivitiesByUser(username)})
    except Exception as e:
        return Response(dumps({'error': str(e)}), status=500, mimetype='application/json')