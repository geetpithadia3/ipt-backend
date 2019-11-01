from flask import Flask

from app.database import DB
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    DB.init()
    bcrypt.init_app(app)
    register_blueprint(app)
    return app

from app.main.controllers.user_api import user_api
def register_blueprint(app):
    """Register blueprints on adding new api files"""
    app.register_blueprint(user_api)



