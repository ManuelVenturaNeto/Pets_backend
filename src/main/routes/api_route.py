# pylint: disable=W0613

import bcrypt
from flask import Blueprint, jsonify, request
from src.security.auth_jwt.token_handler import token_creator
from src.security.auth_jwt.token_verificator import token_verify
from src.infra.repo.user_repository import UserRepository
from src.data.find_user import FindUser
from src.main.composer import (
    register_user_composer,
    register_pet_composer,
    find_user_composer,
    find_pet_composer,
)
from src.main.adapter import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)


# @api_routes_bp.route("/Secret", methods=["GET"])
# @token_verify
# def secret_route(token):

#     # Devemos chegar aqui
#     return jsonify({"data": "Mensagem secreta", "token": token}), 200


@api_routes_bp.route("/auth", methods=["POST"])
def authorization_route():
    """
    athenticate user
    """

    name = request.args.get("name")
    password = request.args.get("password")

    if not name or not password:
        return jsonify({"error": "Missing uid or password"}), 400

    user_repo = UserRepository()
    find_user = FindUser(user_repo)
    user_response = find_user.by_name(name=name)

    if not user_response["Success"] or not user_response["Data"]:
        return jsonify({"error": "User not found"}), 404

    user = user_response["Data"][0]
    user_name = user.name
    hash_password = user.password

    input_password = bcrypt.checkpw(password.encode("utf-8"), hash_password)

    if not input_password:
        return jsonify({"error": "Invalid password"}), 401

    if (user_name == name) and input_password:
        token = token_creator.create(uid=int(user.id))

        return jsonify({"token": token}), 200

    return jsonify({"error": "User Unauthorized"}), 401


@api_routes_bp.route("/api/users", methods=["POST"])
@token_verify
def register_user(token):
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
@token_verify
def register_pet(token):
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
@token_verify
def finder_users(token):
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
@token_verify
def finder_pets(token):
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
