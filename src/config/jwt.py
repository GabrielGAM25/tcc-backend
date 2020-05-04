from flask_jwt import JWT
from datetime import timedelta

from .routes import authentication as routes
from repository.users_repository import UsersRepository
from config.bcrypt import bcrypt

jwt = JWT()

def authenticate(email, password):
    user = UsersRepository.get_user_by_email(email)
    if user and bcrypt.check_password_hash(user.password, password):
        return user

def identity_handler(payload):
    user_id = payload['identity']
    return UsersRepository.get_user_by_id(user_id)

def setup_jwt(app):
    app.config['JWT_AUTH_URL_RULE'] = routes['login']
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=30)
    jwt = JWT(app, authenticate, identity_handler)
