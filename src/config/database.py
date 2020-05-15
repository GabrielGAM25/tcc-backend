from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .environment import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_URL, POSTGRES_DB

db = SQLAlchemy()
migrate = Migrate()

def setup_database(app):
    db_url = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PASSWORD, url=POSTGRES_URL, db=POSTGRES_DB)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
