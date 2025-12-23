import logging
import os
from functools import wraps
import jwt
from flask import jsonify, request
from src.infra.repo.animal_shelter_repository import AnimalShelterRepository
from src.data.find_animal_shelter import FindAnimalShelter
from src.infra.auth_jwt.token_handler import token_creator


def token_verify(function: callable) -> callable:
    """Checking the valid Token and refreshing it. If not valid, return
    Info and stopping client request
    :parram - http request.headers: (AnimalSheltername / Token)
    :return - Json with the corresponding information.
    """
    log = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )



    @wraps(function)
    def decorated(*arg, **kwargs):
        raw_token = request.headers.get("Authorization")
        name = request.args.get("name")
        log.info(f"Verifying token for Animal Shelter: {name}")

        animal_shelter_repo = AnimalShelterRepository()
        find_animal_shelter = FindAnimalShelter(animal_shelter_repo)
        log.info(f"Finding Animal Shelter by name: {name}")

        animal_shelter_response = find_animal_shelter.by_name(name=name)
        animal_shelter = animal_shelter_response["Data"][0]
        uid = animal_shelter.id
        log.info(f"Animal Shelter found with ID: {uid}")

        # Without Token
        if not raw_token and not uid:
            log.info("No token provided in the request.")
            return jsonify({"error": "Bad Request"}), 400

        try:
            token = raw_token.split()[1]
            token_information = jwt.decode(token, key=str(os.getenv("TOKEN_KEY")), algorithms="HS256")
            token_uid = token_information["uid"]

        except jwt.ExpiredSignatureError:
            log.info("Token has expired.")
            return jsonify({"message": "Token is Expired"}), 401

        except jwt.InvalidSignatureError:
            log.info("Token is invalid due to invalid signature.")
            return jsonify({"message": "Token is invalid"}), 401

        except KeyError:
            log.info("Token is invalid due to missing keys.")
            return jsonify({"message": "Token is invalid"}), 401

        if uid and token_uid and (int(token_uid) != int(uid)):
            log.info("Unauthorized access attempt detected.")
            return jsonify({"message": "AnimalShelter Unauthorized"}), 401

        next_token = token_creator.refresh(token)

        log.info("Token verified successfully.")
        return function(next_token, *arg, **kwargs)

    log.info("Token verification decorator created.")
    return decorated
