from flask import Blueprint, jsonify, request, abort
from flask_jwt import jwt_required

from config.routes import users as routes
from services.users import DestroyUser, SearchUser, PersistUser

blueprint = Blueprint('users', __name__)


@blueprint.route(routes['index'], methods=['GET'])
@jwt_required()
def index():
    service = SearchUser()
    users = service.get_all_users()
    return jsonify([user.serialize() for user in users])


@blueprint.route(routes['create'], methods=['POST'])
@jwt_required()
def create():
    user_dictionary = request.get_json()

    service = PersistUser()
    service.create_user(user_dictionary)

    return jsonify(success=True)


@blueprint.route(routes['show'], methods=['GET'])
@jwt_required()
def show(user_id):
    service = SearchUser()
    user = service.get_user_by_id(user_id)
    
    if not user: abort(404)

    return jsonify(user.serialize())


@blueprint.route(routes['destroy'], methods=['DELETE'])
@jwt_required()
def destroy(user_id):
    service = DestroyUser()
    service.delete_user(user_id)
    
    return jsonify(success=True)


@blueprint.route(routes['update'], methods=['PUT'])
@jwt_required()
def update(user_id):
    user_dictionary = request.get_json()

    service = PersistUser()
    service.update_user(user_id, user_dictionary)

    return jsonify(success=True)
