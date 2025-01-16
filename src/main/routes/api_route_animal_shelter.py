from flask import jsonify, request
from src.main.routes.api_route import api_routes_bp
from src.main.composer import (
    register_animal_shelter_composer,
    find_animal_shelter_composer,
)
from src.main.adapter import flask_adapter

# from src.security.auth_jwt.token_verificator import token_verify


@api_routes_bp.route("/api/animal_shelters", methods=["POST"])
def register_animal_shelter():
    """
    register animal_shelter route
    """

    message = {}
    response = flask_adapter(
        request=request, api_route=register_animal_shelter_composer()
    )

    if response.status_code < 300:
        message = {
            "type": "animal_shelters",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "cpf": response.body.cpf,
                "responsible_name": response.body.responsible_name,
                "email": response.body.email,
                "phone_number": response.body.phone_number,
                "address_id": response.body.address_id,
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


@api_routes_bp.route("/api/animal_shelters", methods=["GET"])
def finder_animal_shelters():
    """
    find animal_shelters route
    """

    message = {}
    response = flask_adapter(request=request, api_route=find_animal_shelter_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "animal_shelters",
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
