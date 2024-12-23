from flask import Blueprint, jsonify, request
from src.security.auth_jwt.token_handler import token_creator
from src.security.auth_jwt.token_verificator import token_verify
from src.main.composer import (
    register_user_composer,
    register_pet_composer,
    find_user_composer,
    find_pet_composer,
)
from src.main.adapter import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/secret", methods=["GET"])
@token_verify
def secret_route(token):

    # Devemos chegar aqui
    return jsonify({"data": "Mensagem secreta", "token": token}), 200


@api_routes_bp.route("/auth", methods=["POST"])
def authorization_route():

    token = token_creator.create(uid=12)
    return jsonify({"token": token}), 200


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """
    register user route
    """

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    # Handling errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["POST"])
def register_pet():
    """
    register pet route
    """

    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())

    if response.status_code < 300:
        message = {
            "type": "pets",
            "id": response.body.id,
            "user_attributes": {
                "name": response.body.name,
                "specie": response.body.species,
                "age": response.body.age,
            },
            "relationship": {
                "owner": {
                    "type": "users",
                    "id": response.body.user_id,
                },
            },
        }

        return jsonify({"data": message}), response.status_code

    # Handling errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["GET"])
def finder_users():
    """
    find users route
    """

    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "users",
                    "id": element.id,
                    "attributest": {"name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["GET"])
def finder_pets():
    """
    find pets route
    """

    message = {}
    response = flask_adapter(request=request, api_route=find_pet_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "pets",
                    "id": element.id,
                    "attributest": {
                        "name": element.name,
                        "species": element.species,
                        "age": element.age,
                    },
                    "relationships": {
                        "owner": {"type": "users", "id": element.user_id}
                    },
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
