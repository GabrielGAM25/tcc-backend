from flask_jwt import JWT
from datetime import timedelta

from .routes import authentication as routes
from service.authentication_service import AuthenticationService

def setup_jwt(app):
    app.config['JWT_AUTH_URL_RULE'] = routes['login']
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=30)
    jwt = JWT(
        app,
        AuthenticationService.authenticate,
        AuthenticationService.get_authenticated_user
    )
