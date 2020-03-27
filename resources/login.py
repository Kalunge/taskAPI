from main import Resource, api, fields, create_access_token
from models.usermodel import UserModel, user_schema, users_schema
from werkzeug.security import generate_password_hash

ns_registration = api.namespace('registration', description='User sign up')
ns_login = api.namespace('login', description='Login details')

login_model = api.model('Login_credentials', {
    'email': fields.String(),
    'password': fields.String()
})

registration_model = api.model('Signup_credentials', {
    'full_name': fields.String(),
    'email': fields.String(),
    'password': fields.String()
})


@ns_login.route('')
class Login(Resource):  

    @api.expect(login_model)
    def post(self):
        ''' use this to authenticate users'''
        data = api.payload
        email = data['email']
        if UserModel.check_if_mail_exists(email):
            if UserModel.check_passoword(data['password'], email):
                user_id = UserModel.get_user_id(email)
                access_token = create_access_token(identity=user_id)
                return {'access_Token': access_token}
            else:
                return {'message':'Invalid login credentials'}, 401
        else:
                return {'message':'Invalid login credentials'}, 401

@ns_registration.route('')
class UserRegister(Resource):
    @api.expect(registration_model)
    def post(self):
        '''edit a user by id'''
        data = api.payload
        user = UserModel(full_name=data['full_name'], password=generate_password_hash(data['password']), email=data['email'])
        user.save_to_db()
        return user_schema.dump(user)
