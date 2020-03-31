from flask import Flask, jsonify, Blueprint
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from Configs.DbConfig import DevelopmentConfigs
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.exceptions import BadRequest, Unauthorized, NotFound
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://741de186344745278af2ad034b435340@sentry.io/5181606",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

authorizations = {
    "apikey": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "Type in the *value into the box below**Bearer & where jwt is token",
    }
}

app.config.from_object(DevelopmentConfigs)
app.config['PROPAGATE_EXCEPTIONS'] = True
blueprint = Blueprint('taskApi', __name__, url_prefix='/api/home')


api = Api(blueprint, title='Task management api', description='task manager api', version='1.0', author='Titoh',doc='/doc', authorizations=authorizations)
app.register_blueprint(blueprint)
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


from models.taskmodel import TaskModel


@app.before_first_request
def create_all():
    db.create_all()

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'message':"Bad request"}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'message':"you are not authorized"}), 401

@app.errorhandler(404)
def unauthorized(error):
    return jsonify({'message':"resource not found"}), 404

# jwt._set_error_handler_callbacks(api)


from resources.tasks import *
from resources.user import *
from resources.login import *

@app.route('/')
def home():
    return {'message':'THis is my homepage'}

@app.route('/debug')
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == "__main__":
    app.run(debug=True)
