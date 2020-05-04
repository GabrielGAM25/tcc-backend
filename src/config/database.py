from flask_sqlalchemy import SQLAlchemy

from config.environment import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_URL, POSTGRES_DB

db = SQLAlchemy()

def setup_database(app):
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PASSWORD,url=POSTGRES_URL,db=POSTGRES_DB)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)