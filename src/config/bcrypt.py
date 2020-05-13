from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def setup_bcrypt(app):
    bcrypt.init_app(app)

def generate_password_hash(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password_hash(encrypted_password, plain_text_password):
    return bcrypt.check_password_hash(encrypted_password, plain_text_password)
