from flask import Blueprint, jsonify, abort
from flask_jwt import jwt_required

from config.routes import assessments as routes
from service.assessments_service import AssessmentsService

blueprint = Blueprint('assessments', __name__)


@blueprint.route(routes['index'], methods=['GET'])
@jwt_required()
def index(user_id):
    if user_id is None:
        abort(400)

    assessments = AssessmentsService.get_user_assessments(user_id)
    return jsonify([assessment.serialize() for assessment in assessments])
