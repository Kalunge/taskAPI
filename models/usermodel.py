from main import db, ma
from sqlalchemy import func


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80),nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    tasks = db.relationship('TaskModel', backref='user', lazy=True)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def fetch_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()


class UsersSchema(ma.Schema):
    class Meta:
        fields = ("id", "full_name", "email", "created_at")

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
