from config.routes import users as users_routes, assessments as assessments_routes

from .users_controller import blueprint as users
from .assessments_controller import blueprint as assessments


def register_controllers(app):
    app.register_blueprint(users, url_prefix=users_routes['prefix'])
    app.register_blueprint(assessments, url_prefix=assessments_routes['prefix'])
