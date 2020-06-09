from flask import jsonify

from repositories.users import SearchUserRepository
from repositories.users.errors import UserNotFound
from config.bcrypt import check_password_hash


class AuthenticationService:
    def __init__(self, search_user_repository=SearchUserRepository()):
        self.search_user_repository = search_user_repository

    def authenticate(self, email, password):
        user = self.search_user_repository.get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            return user

    def get_authenticated_user(self, payload):
        user_id = payload['identity']
        try:
            return self.search_user_repository.get_user_by_id(user_id)
        except UserNotFound:
            return None

    def login_response_handler(self, access_token, user):
        return jsonify({
            'access_token': access_token.decode('utf-8'),
            'user': user.serialize(),
        })
