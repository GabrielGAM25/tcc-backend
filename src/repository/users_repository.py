from config.bcrypt import bcrypt
from config.database import db
from model.user import User

class UsersRepository:
    @classmethod
    def get_all_users(cls):
        return User.query.all()

    @classmethod
    def get_user_by_id(cls, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @classmethod
    def create_user(cls, user):
        db.session.add(user)
        db.session.commit()

    @classmethod
    def update_user(cls, user_id, user_data):
        user = cls.get_user_by_id(user_id)

        user.name = user_data['name']
        user.email = user_data['email']
        user.birth_date = user_data['birth_date']

        db.session.commit()

    @classmethod
    def delete_user(cls, user_id):
        User.query.filter_by(id=user_id).delete()
        db.session.commit()

    @classmethod
    def get_user_by_email(cls, email):
        user = User.query.filter_by(email=email).first()
        return user
