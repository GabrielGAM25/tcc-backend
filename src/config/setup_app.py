from controller.api_controller import register_controllers

from .jwt import setup_jwt
from .bcrypt import setup_bcrypt
from .database import setup_database


def setup_app(app):
    app.config['SECRET_KEY'] = 'super-secret'
    setup_database(app)
    setup_bcrypt(app)
    register_controllers(app)
    setup_jwt(app)
