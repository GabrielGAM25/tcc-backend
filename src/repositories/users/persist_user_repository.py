from config.database import db
from models import User
from factories import UserFactory 

from .search_user_repository import SearchUserRepository


class PersistUserRepository:
    def __init__(self, factory=UserFactory, search_repository=SearchUserRepository()):
        self.factory = factory
        self.search_repository = search_repository

    def create_user(self, user):
        user_model = User.from_entity(user)

        db.session.add(user_model)
        db.session.commit()

    def update_user(self, user_id, user):
        user_dictionary = user.to_dictionary()
        user = User.query.filter_by(id=user_id).update(user_dictionary)
        db.session.commit()
