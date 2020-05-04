from flask_jwt import JWT

from repository.users_repository import UsersRepository

def authenticate(email, password):
    user = UsersRepository.get_user_by_email(email)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return UsersRepository.get_user_by_id(user_id)
