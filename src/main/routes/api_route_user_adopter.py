from flask import jsonify, request
from src.main.routes.api_route import api_routes_bp
from src.main.composer import register_user_adopter_composer, find_user_adopter_composer
from src.main.adapter import flask_adapter

# from src.security.auth_jwt.token_verificator import token_verify


@api_routes_bp.route("/api/user_adopters", methods=["POST"])
def register_user_adopter():
    """
    register user_adopter route
    """

    message = {}
    response = flask_adapter(
        request=request, api_route=register_user_adopter_composer()
    )

    if response.status_code < 300:
        message = {
            "type": "user_adopters",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "cpf": response.body.cpf,
                "email": response.body.email,
                "phone_number": response.body.phone_number,
                "address_id": response.body.address_id,
                "pet_id": response.body.pet_id,
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


@api_routes_bp.route("/api/user_adopters", methods=["GET"])
def finder_user_adopters():
    """
    find user_adopters route
    """

    message = {}
    response = flask_adapter(request=request, api_route=find_user_adopter_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "user_adopters",
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
