from flask import Flask
from flask_restx import Api, Resource, fields




app = Flask(__name__)
api = Api(app, title='Task management api', description='task manager api', version='1.0', author='Titoh')

from resources.tasks import *
from resources.user import *

app.run()
