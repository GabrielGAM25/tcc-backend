from datetime import timedelta
from flask_jwt import JWT

from service.authentication_service import AuthenticationService
from .routes import authentication as routes


jwt = JWT(
    None,
    AuthenticationService.authenticate,
    AuthenticationService.get_authenticated_user,
)

jwt.auth_response_handler(AuthenticationService.login_response_handler)

def setup_jwt(app):
    app.config['JWT_AUTH_URL_RULE'] = routes['login']
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=30)
    jwt.init_app(app)
