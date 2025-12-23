import logging
import bcrypt
from flask import Blueprint, jsonify, request
from src.infra.auth_jwt.token_handler import token_creator
from src.infra.repo.animal_shelter_repository import AnimalShelterRepository
from src.data.find_animal_shelter import FindAnimalShelter

api_routes_bp = Blueprint("api_routes", __name__)

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)


@api_routes_bp.route("/auth", methods=["POST"])
def authorization_route():
    """
    athenticate animal_shelter
    """

    name = request.args.get("name")
    password = request.args.get("password")

    if not name or not password:
        log.error("Missing name or password")
        return jsonify({"error": "Missing uid or password"}), 400

    animal_shelter_repo = AnimalShelterRepository()
    find_animal_shelter = FindAnimalShelter(animal_shelter_repo)
    animal_shelter_response = find_animal_shelter.by_name(name=name)

    if not animal_shelter_response["Success"] or not animal_shelter_response["Data"]:
        log.error("AnimalShelter not found")
        return jsonify({"error": "AnimalShelter not found"}), 404

    animal_shelter = animal_shelter_response["Data"][0]
    animal_shelter_name = animal_shelter.name
    hash_password = bytes.fromhex(animal_shelter.password[2:])

    input_password = bcrypt.checkpw(password.encode("utf-8"), hash_password)
    log.info(f"Authentication attempt for Animal Shelter: {animal_shelter_name}")

    if not input_password:
        log.error("AnimalShelter not found")
        return jsonify({"error": "AnimalShelter not found"}), 404

    if (animal_shelter_name == name) and input_password:
        token = token_creator.create(uid=int(animal_shelter.id))

        log.info(f"Animal Shelter {animal_shelter_name} authenticated successfully")
        return jsonify({"token": token}), 200

    log.error("AnimalShelter Unauthorized")
    return jsonify({"error": "AnimalShelter Unauthorized"}), 401
