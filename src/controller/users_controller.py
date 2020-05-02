from flask import Blueprint, jsonify
from config.routes import users as routes

users_controller = Blueprint('users_controller', __name__)

@users_controller.route(routes['index'])
def index():
    return jsonify({'id': 10})