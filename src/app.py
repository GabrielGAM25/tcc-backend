from flask import Flask
from controller.users_controller import users_controller

app = Flask(__name__)

app.register_blueprint(users_controller)

if __name__ == "__main__":
    app.run()