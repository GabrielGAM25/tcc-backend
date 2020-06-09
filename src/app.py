from flask import Flask

from config.setup_app import setup_app
from seeds import seed_database, clear_database

app = Flask(__name__)
setup_app(app)

@app.cli.command('db:seed')
def seed_db():
    seed_database()


@app.cli.command('db:clear')
def clear_db():
    clear_database()


if __name__ == "__main__": 
    app.run()
