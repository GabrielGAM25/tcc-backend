from flask import Flask
from flask_script import Manager

from config.setup_app import setup_app
from seed import seed_database, clear_database

app = Flask(__name__)
setup_app(app)

manager = Manager(app)

@manager.command
def seed_db():
    seed_database()

@manager.command
def clear_db():
    clear_database()

if __name__ == "__main__":
    manager.run()
