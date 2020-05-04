from flask import Blueprint, jsonify, request, abort
from flask_jwt import jwt_required

from config.routes import users as routes
from service.users_service import UsersService

users = Blueprint('users', __name__)

@users.route(routes['index'], methods=['GET'])
def index():
    users = UsersService.get_all_users()
    return jsonify([user.serialize() for user in users])

@users.route(routes['create'], methods=['POST'])
def create():
    user_data = request.get_json()
    UsersService.create_user(user_data)
    return jsonify(success=True)

@users.route(routes['show'], methods=['GET'])
def show(user_id):
    user = UsersService.get_user_by_id(user_id)
    if(user == None):
        abort(404)

    return jsonify(user.serialize())

@users.route(routes['destroy'], methods=['DELETE'])
@jwt_required()
def destroy(user_id):
    UsersService.delete_user(user_id)
    return jsonify(success=True)

@users.route(routes['update'], methods=['PUT'])
def update(user_id):
    user_data = request.get_json()
    UsersService.update_user(user_id, user_data)
    
    return jsonify(success=True)
