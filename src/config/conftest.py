from flask import Flask
import pytest

from config.setup_app import setup_app

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['ENV']='test'
    setup_app(app)
    return app
