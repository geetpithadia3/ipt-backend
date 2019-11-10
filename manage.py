
import unittest

from flask_script import Manager
# Manager file
# This file is the entry point to the application 
from app import create_app
from flask_cors import CORS, cross_origin
app = create_app()
app.app_context().push()
manager = Manager(app)
CORS(app, support_credentials=True)

from flask import Flask, send_from_directory

@app.route('/')
def index():
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(404)
def errorHandler(e):
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')

@manager.command
def run():
    app.run(debug=True)

@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern = 'test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()