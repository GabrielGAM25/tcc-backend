from flask import Blueprint, jsonify, request, abort
from flask_jwt import jwt_required

from config.routes import users as routes
from service.users_service import UsersService

blueprint = Blueprint('users', __name__)


@blueprint.route(routes['index'], methods=['GET'])
@jwt_required()
def index():
    users = UsersService.get_all_users()
    return jsonify([user.serialize() for user in users])


@blueprint.route(routes['create'], methods=['POST'])
@jwt_required()
def create():
    user_data = request.get_json()
    UsersService.create_user(user_data)
    return jsonify(success=True)


@blueprint.route(routes['show'], methods=['GET'])
@jwt_required()
def show(user_id):
    user = UsersService.get_user_by_id(user_id)
    if user is None:
        abort(404)

    return jsonify(user.serialize())


@blueprint.route(routes['destroy'], methods=['DELETE'])
@jwt_required()
def destroy(user_id):
    UsersService.delete_user(user_id)
    return jsonify(success=True)


@blueprint.route(routes['update'], methods=['PUT'])
@jwt_required()
def update(user_id):
    user_data = request.get_json()
    UsersService.update_user(user_id, user_data)

    return jsonify(success=True)
