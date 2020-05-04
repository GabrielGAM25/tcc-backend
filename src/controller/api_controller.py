from config.routes import users as users_routes

from .users_controller import users

def register_controllers(app):
    app.register_blueprint(users, url_prefix=users_routes['prefix'])
