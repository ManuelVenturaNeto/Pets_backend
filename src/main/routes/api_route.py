from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer
from src.main.adapter import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """
    register user route
    """

    message = None
    response = flask_adapter(request=request, api_route=register_user_composer())

    message = {
        "Type": "Users",
        "id": response.body.id,
        "attributes": {"name": response.body.name},
    }

    return jsonify({"data": message}), response.status_code
