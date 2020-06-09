from config.bcrypt import generate_password_hash
from models import User
from repositories.users import SearchUserRepository
from repositories.users.errors import UserNotFound


class SearchUser:
    def __init__(self, search_user_repository=SearchUserRepository()):
        self.repository = search_user_repository

    def get_all_users(self):
        return self.repository.get_all_users()

    def get_user_by_id(self, user_id):
        try:
            return self.repository.get_user_by_id(user_id)
        except UserNotFound:
            return None
