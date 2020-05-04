from flask import Flask

from config.jwt import setup_jwt
from config.bcrypt import setup_bcrypt
from config.database import setup_database
from controller.api_controller import register_controllers


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret'
    setup_database(app)
    setup_bcrypt(app)
    register_controllers(app)
    setup_jwt(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
