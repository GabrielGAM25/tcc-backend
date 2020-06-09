from config.bcrypt import generate_password_hash
from models import User
from repositories.users import DestroyUserRepository


class DestroyUser:
    def __init__(self, repository=DestroyUserRepository()):
        self.repository = repository
    
    def delete_user(self, user_id):
        self.repository.delete_user(user_id)
