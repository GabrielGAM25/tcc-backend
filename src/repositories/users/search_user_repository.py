from models import User
from factories import UserFactory

from .errors import UserNotFound


class SearchUserRepository:
    def __init__(self, factory=UserFactory):
        self.factory = factory or UserFactory

    def get_all_users(self):
        users = User.query.order_by(User.id)
        return self.factory.from_models(users)

    def get_user_by_id(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            raise UserNotFound

        return self.factory.from_model(user)

    def get_user_by_email(self, email):
        user = User.query.filter_by(email=email).first()
        return self.factory.from_model(user)
