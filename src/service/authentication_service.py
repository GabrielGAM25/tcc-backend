from repository.users_repository import UsersRepository
from config.bcrypt import bcrypt
class AuthenticationService:
    @classmethod
    def authenticate(cls, email, password):
        user = UsersRepository.get_user_by_email(email)
        if user and bcrypt.check_password_hash(user.password, password):
            return user

    @classmethod
    def get_authenticated_user(cls, payload):
        user_id = payload['identity']
        return UsersRepository.get_user_by_id(user_id)
