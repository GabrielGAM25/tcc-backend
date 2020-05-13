from flask_cors import CORS

from controller.api_controller import register_controllers

from .database import setup_database
from .bcrypt import setup_bcrypt
from .jwt import setup_jwt


def setup_app(app):
    # Prevent the json parser from sorting response JSON keys
    app.config['JSON_SORT_KEYS'] = False

    # Setup the connection to the database
    setup_database(app)

    # Setup BCrypt for password handling
    setup_bcrypt(app)

    # Register the API endpoints
    register_controllers(app)

    # Setup JWT for user authentication
    app.config['SECRET_KEY'] = 'jamal`s-super-secret'
    setup_jwt(app)

    # Fixes CORS issues
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)
