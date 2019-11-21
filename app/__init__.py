# Initialization file
# This file sets up the application for running

from flask import Flask
from app.database import DB
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='../web/static')
    app.secret_key = 'hack me'
    DB.init()
    bcrypt.init_app(app)
    register_blueprint(app)
    return app

from app.main.controllers.user_api import user_api
from app.main.controllers.studentactivity_api import studentactivity_api
from app.main.controllers.company_api import company_api
from app.main.controllers.jobPostings_api import jobPostings_api
from app.main.controllers.dashboard_api import dashboard_api
def register_blueprint(app):
    """Register blueprints on adding new api files"""
    app.register_blueprint(user_api, url_prefix='/api/user')
    app.register_blueprint(studentactivity_api, url_prefix='/api/activity')
    app.register_blueprint(company_api, url_prefix='/api/company')
    app.register_blueprint(jobPostings_api, url_prefix='/api/posting')
    app.register_blueprint(dashboard_api, url_prefix='/api/dashboard')