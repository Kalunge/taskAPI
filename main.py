from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from Configs.DbConfig import DevelopmentConfigs
from flask_marshmallow import Marshmallow




app = Flask(__name__)
app.config.from_object(DevelopmentConfigs)
api = Api(app, title='Task management api', description='task manager api', version='1.0', author='Titoh')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models.taskmodel import TaskModel

@app.before_first_request
def create_all():
    db.create_all()

from resources.tasks import *
from resources.user import *

if __name__ == "__main__":
    app.run(debug=True)
