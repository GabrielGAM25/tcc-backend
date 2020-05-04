from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def setup_bcrypt(app):
    bcrypt.init_app(app)
