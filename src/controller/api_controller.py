from config.routes import users as users_routes

from .users_controller import blueprint as users


def register_controllers(app):
    app.register_blueprint(users, url_prefix=users_routes['prefix'])
