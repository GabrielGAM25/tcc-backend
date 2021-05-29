from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .environment import get_env_variable

db = SQLAlchemy()
migrate = Migrate()


def create_db_url(url, user, pw, db):
    return f"postgresql+psycopg2://{user}:{pw}@{url}/{db}"


def get_db_config(environment):
    if environment == "development":
        POSTGRES_USER = get_env_variable("DEV_POSTGRES_USER")
        POSTGRES_PW = get_env_variable("DEV_POSTGRES_PW")
        POSTGRES_URL = get_env_variable("DEV_POSTGRES_URL")
        POSTGRES_DB = get_env_variable("DEV_POSTGRES_DB")

    elif environment == "test":
        POSTGRES_USER = get_env_variable("TEST_POSTGRES_USER")
        POSTGRES_PW = get_env_variable("TEST_POSTGRES_PW")
        POSTGRES_URL = get_env_variable("TEST_POSTGRES_URL")
        POSTGRES_DB = get_env_variable("TEST_POSTGRES_DB")

    elif environment == "production":
        POSTGRES_USER = get_env_variable("PROD_POSTGRES_USER")
        POSTGRES_PW = get_env_variable("PROD_POSTGRES_PW")
        POSTGRES_URL = get_env_variable("PROD_POSTGRES_URL")
        POSTGRES_DB = get_env_variable("PROD_POSTGRES_DB")
    
    else:
        raise Exception('Invalid value for FLASK_ENV')

    return create_db_url(POSTGRES_URL, POSTGRES_USER, POSTGRES_PW, POSTGRES_DB)


def setup_database(app):
    db_url = get_db_config(app.config['ENV'])
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
