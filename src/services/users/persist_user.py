from config.bcrypt import generate_password_hash

from factories import UserFactory
from repositories.users import PersistUserRepository, SearchUserRepository


class PersistUser:
    def __init__(self, factory=UserFactory, persist_repository=PersistUserRepository(), search_repository=SearchUserRepository()):
        self.factory = factory
        self.persist_repository = persist_repository
        self.search_repository = search_repository

    def create_user(self, user_dictionary):
        user_dictionary['password'] = generate_password_hash(user_dictionary['password'])
        user = self.factory.from_dictionary(user_dictionary)
        self.persist_repository.create_user(user)

    def update_user(self, user_id, user_dictionary):
        user = self.factory.from_dictionary(user_dictionary)
        self.persist_repository.update_user(user_id, user)
