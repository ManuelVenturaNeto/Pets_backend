import logging
from flask import jsonify, request
from src.main.routes.api_route import api_routes_bp
from src.main.composer import (
    register_specie_composer,
    find_specie_composer,
)
from src.main.adapter import flask_adapter

# from src.infra.auth_jwt.token_verificator import token_verify

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)



@api_routes_bp.route("/api/species", methods=["POST"])
def register_specie():
    """
    register animal_shelter route
    """

    message = {}
    response = flask_adapter(request=request, api_route=register_specie_composer())
    log.info(f"Register Specie response status: {response.status_code}")

    if response.status_code < 300:
        message = {
            "type": "species",
            "id": response.body.id,
            "attributes": {"specie_name": response.body.specie_name},
        }

        log.info(f"Specie registered successfully: {message}")
        return jsonify({"data": message}), response.status_code

    # Handling errors
    log.error(f"Error registering Specie: {response.body['error']}")
    return jsonify({"error": {"status": response.status_code, "title": response.body["error"]}}), response.status_code



@api_routes_bp.route("/api/species", methods=["GET"])
def finder_species():
    """
    find species route
    """

    message = {}
    response = flask_adapter(request=request, api_route=find_specie_composer())
    log.info(f"Finding Species response status: {response.status_code}")

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

        log.info(f"Species found successfully: {message}")
        return jsonify({"data": message}), response.status_code

    # Handling Errors
    log.error(f"Error finding Species: {response.body['error']}")
    return jsonify({"error": {"status": response.status_code, "title": response.body["error"]}}), response.status_code
