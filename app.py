from flask import Flask
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app, title='Task management api', description='task manager api',version='1.0', author='Titoh')

ns_tasks = api.namespace('tasks', description='All tasks regarding tasks')
ns_users = api.namespace('users', description='all tasks regarding users')

task_list = [
    {'id':1, 'title':'learn flask-restx', 'description':'learn the basices'},
    {'id':2, 'title':'learn vue js', 'description':'learn the basices'},
    {'id':3, 'title':'learn docker', 'description':'learn the basices'}
]

@ns_tasks.route('')
class TasksList(Resource):
    def get(self):
        """ use this ednpoint to get a list of tasks """
        return task_list, 200

    def post(self):
        """ use this ednpoint to add new tasks """
        _id = len(task_list) + 1
        data = api.payload
        data['id'] = _id
        task_list.append(data)
        return data, 201


@ns_tasks.route('/<int:_id>')
class Task(Resource):
    def get(self, _id):
        '''retrieve a task by it's id'''
        return next(filter(lambda x:x['id'] == _id, task_list))
        # return task_list[_id-1]
        

    def put(self, _id):
        '''edit a task by it's id'''
        data = api.payload
        task = next(filter(lambda x:x['id'] == _id, task_list))
        if task:
            # task['id'] = data['id']
            task['title'] = data['title']
            task['description'] = data['description']
            return task, 200
        return 'Task does not exist', 404
        




    def delete(self, _id):
        '''delete a task by it's id'''

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


app.run()
