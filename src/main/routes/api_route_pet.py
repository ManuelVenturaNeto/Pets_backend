from flask import jsonify, request
from src.main.routes.api_route import api_routes_bp
from src.main.composer import (
    register_pet_composer,
    find_pet_composer,
)
from src.main.adapter import flask_adapter

# from src.infra.auth_jwt.token_verificator import token_verify


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
            "animal_shelter_attributes": {
                "name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
                "adopted": response.body.adopted,
            },
            "relationship": {
                "owner": {
                    "type": "animal_shelters",
                    "id": response.body.animal_shelter_id,
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
                        "specie": element.specie,
                        "age": element.age,
                    },
                    "relationships": {
                        "owner": {
                            "type": "animal_shelters",
                            "id": element.animal_shelter_id,
                        }
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
