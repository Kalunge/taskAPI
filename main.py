from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from Configs.DbConfig import DevelopmentConfigs
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config.from_object(DevelopmentConfigs)
api = Api(app, title='Task management api', description='task manager api', version='1.0', author='Titoh')
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

from models.taskmodel import TaskModel


@app.before_first_request
def create_all():
    db.create_all()

from resources.tasks import *
from resources.user import *
from resources.login import *


if __name__ == "__main__":
    app.run(debug=True)
