from flask import Blueprint, request, abort, make_response, jsonify
from app.blueprints.models.model import (User)

record_blueprint = Blueprint("record_api", __name__)


@record_blueprint.route("", methods=['POST'])
def create():
    if not request.is_json:
        abort(400, description="Missing JSON in request")
    data = request.get_json()
    required_data = {"first_name", "last_name", "age"}
    if not all(key in data for key in required_data):
        abort(400, description="Missing required parameters")

    user = User.create_user(data.get("first_name"), data.get("last_name"), data.get("age"))
    data = {"User": user.to_dict()}
    return make_response(jsonify(data), 201)
