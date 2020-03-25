from main import db, ma
from sqlalchemy import func

class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def create_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    @classmethod
    def fetch_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.commit()


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "user_id", "completed", "created_at")

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
