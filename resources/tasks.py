from main import Resource, api, fields
from models.taskmodel import TaskModel, task_schema, tasks_schema

# namespace
ns_tasks = api.namespace('tasks', description='All tasks regarding tasks')


# models
task_model = api.model('Task', {
    'title':fields.String(),
    'description':fields.String(),
    'user_id':fields.Integer()
})

@ns_tasks.route('')
class TasksList(Resource):
    def get(self):
        """ use this ednpoint to get a list of tasks """
        return tasks_schema.dump(TaskModel.fetch_all()), 200

    @api.expect(task_model)
    def post(self):
        """ use this ednpoint to add a new task """
        data = api.payload
        task = TaskModel(**data)
        task.create_record()
        return task_schema.dump(task)



@ns_tasks.route('/<int:_id>')
class Task(Resource):
    def get(self, _id):
        '''retrieve a task by it's id'''
        # task =  TaskModel.fetch_by_id(_id)
        # return task_schema.dump(task), 200
        tasks = TaskModel.fetch_all()
        task = next(filter(lambda x: x.id==_id, tasks), None)
        if task:
           return task_schema.dump(task)
        else:
            return {'message':'task doesnot exist'}

        # return task_list[_id-1]
        
    @api.expect(task_model)
    def put(self, _id):
        '''edit a task by it's id'''
        data = api.payload
        tasks = TaskModel.fetch_all()
        task = next(filter(lambda x:  x.id==_id, tasks), None)
        if task:
            if u'title' in data:
                task.title = data['title']
            if u'description' in data:
                task.description = data['description']
            task.save_to_db()
            return task_schema.dump(task), 200
        else:
            return {'message':'Task does not exist'}, 404
        
    def delete(self, _id):
        '''delete a task by it's id'''
        tasks = TaskModel.fetch_all()
        task = next(filter(lambda x:  x.id==_id, tasks), None)
        if task:
            task.delete_from_db()
            return {'message':'deleted successfully'}, 200
        else:
            return {'message':'task does not exist'}, 404