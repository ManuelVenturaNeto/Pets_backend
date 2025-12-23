from faker import Faker
from src.data.test import FindPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_pets_controller import FindPetController

faker = Faker("pt_BR")


def test_route():
    """
    testing find pet use case
    """

    find_pet_animal_shelter_case = FindPetSpy(PetRepositorySpy())
    find_pet_route = FindPetController(find_pet_animal_shelter_case)

    attributes = {
        "pet_id": faker.random_number(digits=5),
        "animal_shelter_id": faker.random_number(digits=5),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_route.route(http_request)
    # Testing input
    assert find_pet_animal_shelter_case.by_pet_id_and_animal_shelter_id_param["pet_id"] == attributes["pet_id"]
    assert find_pet_animal_shelter_case.by_pet_id_and_animal_shelter_id_param["animal_shelter_id"] == attributes["animal_shelter_id"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body



def test_route_error_400():
    """
    testing find pet use case
    """

    find_pet_animal_shelter_case = FindPetSpy(PetRepositorySpy())
    find_pet_route = FindPetController(find_pet_animal_shelter_case)

    attributes = {}

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_route.route(http_request)
    # Testing input
    assert not find_pet_animal_shelter_case.by_pet_id_and_animal_shelter_id_param

    # Testing output
    assert http_response.status_code == 400
    assert "error" in http_response.body



def test_route_error_422():
    """
    testing find pet use case
    """

    find_pet_animal_shelter_case = FindPetSpy(PetRepositorySpy())
    find_pet_route = FindPetController(find_pet_animal_shelter_case)

    attributes = {
        "id": faker.random_number(digits=5),
        "animal_id": faker.random_number(digits=5),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_route.route(http_request)
    # Testing input
    assert not find_pet_animal_shelter_case.by_pet_id_and_animal_shelter_id_param

    # Testing output
    assert http_response.status_code == 422
    assert "error" in http_response.body
