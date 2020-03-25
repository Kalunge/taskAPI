from main import api, Resource, fields
from models.usermodel import UserModel, user_schema, users_schema

ns_users = api.namespace('users', description='all tasks regarding users')

user_model = api.model('User', {
    'full_name': fields.String(),
    'email': fields.String(),
    'password': fields.String()
})


@ns_users.route('')
class UsersList(Resource):
    def get(self):
        '''return a list of users'''
        return users_schema.dump(UserModel.fetch_all())

    @api.expect(user_model)
    def post(self):
        '''edit a user by id'''
        data = api.payload
        user = UserModel(**data)
        user.save_to_db()
        return user_schema.dump(user)


@ns_users.route('/<int:_id>')
class Users(Resource):
    def get(self, _id):
        '''Retrieve a user by id'''
        user = UserModel.fetch_by_id(_id)
        return user_schema.dump(user)

    def delete(self, _id):
        '''delete a user by id'''
        user = UserModel.fetch_by_id(_id)
        if user:
            user.delete_from_db()
            return {'message': 'user deleted successfully'}
        else:
            return {'message': 'That user does not exist'}
           