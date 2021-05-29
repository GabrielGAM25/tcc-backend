from config.routes import users as users_routes, assessments as assessments_routes, exercises as exercises_routes

from .users_controller import blueprint as users
from .assessments_controller import blueprint as assessments
from .exercises_controller import blueprint as exercises


def register_controllers(app):
    app.register_blueprint(users, url_prefix=users_routes['prefix'])
    app.register_blueprint(assessments, url_prefix=assessments_routes['prefix'])
    app.register_blueprint(exercises, url_prefix=exercises_routes['prefix'])
