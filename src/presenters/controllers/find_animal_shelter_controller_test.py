from faker import Faker
from src.data.test import FindAnimalShelterSpy
from src.infra.test import AnimalShelterRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_animal_shelter_controller import FindAnimalShelterController

faker = Faker("pt_BR")


def test_route():
    """
    testing route method
    """

    find_animal_shelter_use_case = FindAnimalShelterSpy(AnimalShelterRepositorySpy())
    find_animal_shelter_controller = FindAnimalShelterController(
        find_animal_shelter_use_case
    )
    http_request = HttpRequest(
        query={
            "animal_shelter_id": faker.random_number(digits=5),
            "animal_shelter_name": faker.name(),
        }
    )

    response = find_animal_shelter_controller.route(http_request)

    # testing inputs
    assert find_animal_shelter_use_case.by_id_and_name_param["animal_shelter_id"] == http_request.query["animal_shelter_id"]
    assert find_animal_shelter_use_case.by_id_and_name_param["name"] == http_request.query["animal_shelter_name"]

    # testing outputs
    assert response.status_code == 200
    assert response.body



def test_route_error_400():
    """
    testing route method
    """

    find_animal_shelter_use_case = FindAnimalShelterSpy(AnimalShelterRepositorySpy())
    find_animal_shelter_controller = FindAnimalShelterController(
        find_animal_shelter_use_case
    )
    http_request = HttpRequest()

    response = find_animal_shelter_controller.route(http_request)

    # testing inputs
    assert not find_animal_shelter_use_case.by_id_and_name_param
    assert not find_animal_shelter_use_case.by_id_param
    assert not find_animal_shelter_use_case.by_name_param

    # testing outputs
    assert response.status_code == 400
    assert "error" in response.body



def test_route_error_422():
    """
    testing route method
    """

    find_animal_shelter_use_case = FindAnimalShelterSpy(AnimalShelterRepositorySpy())
    find_animal_shelter_controller = FindAnimalShelterController(
        find_animal_shelter_use_case
    )
    http_request = HttpRequest(
        query={
            "invalid_entry": faker.random_number(digits=5),
            "other_invalidy_entry": faker.name(),
        }
    )

    response = find_animal_shelter_controller.route(http_request)

    # testing inputs
    assert not find_animal_shelter_use_case.by_id_and_name_param
    assert not find_animal_shelter_use_case.by_id_param
    assert not find_animal_shelter_use_case.by_name_param

    # testing outputs
    assert response.status_code == 422
    assert "error" in response.body
