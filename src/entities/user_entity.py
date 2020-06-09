from config.bcrypt import generate_password_hash


class UserEntity():
    def __init__(self, name, email, birth_date, id_=None, encrypted_password=None, password=None):
        self.id = id_
        self.name = name
        self.email = email
        self.password = encrypted_password or generate_password_hash(password)
        self.birth_date = birth_date

    def __repr__(self):
        return f'<User id:{self.id} email:{self.email}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birth_date': self.birth_date,
        }

    def to_dictionary(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'birth_date': self.birth_date,
        }
