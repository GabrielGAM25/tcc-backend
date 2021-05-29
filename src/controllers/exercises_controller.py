from flask import Blueprint, jsonify, abort
from flask_jwt import jwt_required

from config.routes import exercises as routes
from services.exercises import SearchExercise

blueprint = Blueprint('exercises', __name__)


@blueprint.route(routes['index'], methods=['GET'])
@jwt_required()
def index():
    service = SearchExercise()
    exercises = service.get_exercises()
    return jsonify([exercise.serialize() for exercise in exercises])
