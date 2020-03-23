from main import api, fields, Resource

ns_users = api.namespace('users', description='all tasks regarding users')


@ns_users.route('')
class UsersList(Resource):
    def get(self):
        '''return a list of users'''


@ns_users.route('/<int:id>')
class Users(Resource):
    def get(self, _id):
        '''Retrieve a user by id'''

    def put(self, _id):
        '''edit a user by id'''

    def delete(self, _id):
        '''delete a user by id'''