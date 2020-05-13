from flask import jsonify

from repository.users_repository import UsersRepository
from config.bcrypt import check_password_hash


class AuthenticationService:
    @classmethod
    def authenticate(cls, email, password):
        user = UsersRepository.get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            return user

    @classmethod
    def get_authenticated_user(cls, payload):
        user_id = payload['identity']
        return UsersRepository.get_user_by_id(user_id)

    @classmethod
    def login_response_handler(cls, access_token, user):
        return jsonify({
            'access_token': access_token.decode('utf-8'),
            'user': user.serialize(),
        })
