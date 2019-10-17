from flask import Flask
from flask_bcrypt import Bcrypt
from app.main.controllers.user_api import user_api
from app.database import DB

flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    flask_bcrypt.init_app(app)
    DB.init()
    register_blueprint(app)
    return app


def register_blueprint(app):
    """Register blueprints on adding new api files"""
    app.register_blueprint(user_api)
