from faker import Faker
from src.data.test import FindPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_pets_controller import FindPetController

faker = Faker()


def test_route():
    """
    testing find pet use case
    """

    find_pet_user_case = FindPetSpy(PetRepositorySpy())
    find_pet_route = FindPetController(find_pet_user_case)

    attributes = {
        "pet_id": faker.random_number(digits=5),
        "user_id": faker.random_number(digits=5),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_route.route(http_request)
    # Testing input
    assert (
        find_pet_user_case.by_pet_id_and_user_id_param["pet_id"] == attributes["pet_id"]
    )
    assert (
        find_pet_user_case.by_pet_id_and_user_id_param["user_id"]
        == attributes["user_id"]
    )

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body
