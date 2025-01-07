# pylint: disable=W0613

import bcrypt
from flask import Blueprint, jsonify, request
from src.security.auth_jwt.token_handler import token_creator
from src.security.auth_jwt.token_verificator import token_verify
from src.infra.repo.animal_shelter_repository import AnimalShelterRepository
from src.data.find_animal_shelter import FindAnimalShelter
from src.main.composer import (
    register_animal_shelter_composer,
    register_pet_composer,
    find_animal_shelter_composer,
    find_pet_composer,
    register_specie_composer,
    find_specie_composer,
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
    athenticate animal_shelter
    """

    name = request.args.get("name")
    password = request.args.get("password")

    if not name or not password:
        return jsonify({"error": "Missing uid or password"}), 400

    animal_shelter_repo = AnimalShelterRepository()
    find_animal_shelter = FindAnimalShelter(animal_shelter_repo)
    animal_shelter_response = find_animal_shelter.by_name(name=name)

    if not animal_shelter_response["Success"] or not animal_shelter_response["Data"]:
        return jsonify({"error": "AnimalShelter not found"}), 404

    animal_shelter = animal_shelter_response["Data"][0]
    animal_shelter_name = animal_shelter.name
    hash_password = animal_shelter.password

    input_password = bcrypt.checkpw(password.encode("utf-8"), hash_password)

    if not input_password:
        return jsonify({"error": "Invalid password"}), 401

    if (animal_shelter_name == name) and input_password:
        token = token_creator.create(uid=int(animal_shelter.id))

        return jsonify({"token": token}), 200

    return jsonify({"error": "AnimalShelter Unauthorized"}), 401


@api_routes_bp.route("/api/animal_shelters", methods=["POST"])
def register_animal_shelter():
    """
    register animal_shelter route
    """

    message = {}
    response = flask_adapter(request=request, api_route=register_animal_shelter_composer())

    if response.status_code < 300:
        message = {
            "type": "animal_shelters",
            "id": response.body.id,
            "attributes": {"name": response.body.name, 
                           "cpf": response.body.cpf,
                           "responsible_name": response.body.responsible_name,
                           "email": response.body.email,
                           "phone_number": response.body.phone_number,
                           "address_id": response.body.address_id},
        }

        return jsonify({"data": message}), response.status_code

    # Handling errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )

@api_routes_bp.route("/api/species", methods=["POST"])
def register_specie():
    """
    register animal_shelter route
    """

    message = {}
    response = flask_adapter(request=request, api_route=register_specie_composer())

    if response.status_code < 300:
        message = {
            "type": "species",
            "id": response.body.id,
            "attributes": {"specie_name": response.body.specie_name},
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
            "animal_shelter_attributes": {
                "name": response.body.name,
                "specie": response.body.species,
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
    
@api_routes_bp.route("/api/species", methods=["GET"])
def finder_species():
    """
    find species route
    """

    message = {}
    response = flask_adapter(request=request, api_route=find_specie_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "species",
                    "id": element.id,
                    "attributest": {"specie_name": element.specie_name},
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
                        "owner": {"type": "animal_shelters", "id": element.animal_shelter_id}
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
