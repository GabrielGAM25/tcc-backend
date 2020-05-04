from config.bcrypt import bcrypt
from model.user import User
from repository.users_repository import UsersRepository

class UsersService:
    @classmethod
    def get_all_users(cls):
        return UsersRepository.get_all_users()

    @classmethod
    def get_user_by_id(cls, user_id):
        return UsersRepository.get_user_by_id(user_id)
    
    @classmethod
    def create_user(cls, user_data):
        name = user_data['name']
        email = user_data['email']
        password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
        birth_date = user_data['birth_date']

        user = User(
            name=name,
            email=email,
            password=password,
            birth_date=birth_date,
        )
        UsersRepository.create_user(user)

    @classmethod
    def update_user(cls, user_id, user_data):
        UsersRepository.update_user(user_id, user_data)

    @classmethod
    def delete_user(cls, user_id):
        UsersRepository.delete_user(user_id)
