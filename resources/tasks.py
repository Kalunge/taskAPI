from main import Resource, api, fields

# namespace
ns_tasks = api.namespace('tasks', description='All tasks regarding tasks')



task_list = [
    {'id':1, 'title':'learn flask-restx', 'description':'learn the basices'},
    {'id':2, 'title':'learn vue js', 'description':'learn the basices'},
    {'id':3, 'title':'learn docker', 'description':'learn the basices'}
]
# models
task_model = api.model('Task', {
    'title':fields.String(),
    'description':fields.String()
})

@ns_tasks.route('')
class TasksList(Resource):
    def get(self):
        """ use this ednpoint to get a list of tasks """
        return task_list, 200

    @api.expect(task_model)
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
        return next(filter(lambda x: x['id'] == _id, task_list))
        # return task_list[_id-1]
        
    @api.expect(task_model)
    def put(self, _id):
        '''edit a task by it's id'''
        data = api.payload
        task = next(filter(lambda x: x['id'] == _id, task_list), None)
        if task:
            if u'title' in data:
                task['title'] = data['title']
            if u'description' in data:
                task['description'] = data['description']
            return task, 200
        return 'Task does not exist', 404
        
    def delete(self, _id):
        '''delete a task by it's id'''
        global task_list
        task_list = list(filter(lambda x: x['id'] != _id, task_list))
        return {'message':'task deleted successfully'}, 200