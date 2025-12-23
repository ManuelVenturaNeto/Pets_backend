import logging
from faker import Faker
from src.data.test import FindUserAdopterSpy
from src.infra.test import UserAdopterRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_adopter_controller import FindUserAdopterController

faker = Faker("pt_BR")


def test_route_by_user_adopter_id():
    """
    testing find user_adopter use case
    """

    find_user_adopter_animal_shelter_case = FindUserAdopterSpy(
        UserAdopterRepositorySpy()
    )
    find_user_adopter_route = FindUserAdopterController(
        find_user_adopter_animal_shelter_case
    )

    attributes = {"user_adopter_id": faker.random_number(digits=5)}

    http_request = HttpRequest(query=attributes)

    http_response = find_user_adopter_route.route(http_request)
    # Testing input
    assert find_user_adopter_animal_shelter_case.by_user_adopter_id_param["user_adopter_id"] == attributes["user_adopter_id"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body



def test_route_by_pet_id():
    """
    testing find user_adopter use case
    """

    find_user_adopter_animal_shelter_case = FindUserAdopterSpy(UserAdopterRepositorySpy())
    find_user_adopter_route = FindUserAdopterController(find_user_adopter_animal_shelter_case)

    attributes = {"pet_id": faker.random_number(digits=15)}

    http_request = HttpRequest(query=attributes)

    http_response = find_user_adopter_route.route(http_request)

    # Testing input
    assert find_user_adopter_animal_shelter_case.by_pet_id_param["pet_id"] == attributes["pet_id"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body



def test_route_by_user_adopter_informations():
    """
    testing find user_adopter use case
    """

    find_user_adopter_animal_shelter_case = FindUserAdopterSpy(UserAdopterRepositorySpy())
    find_user_adopter_route = FindUserAdopterController(find_user_adopter_animal_shelter_case)

    attributes = {"name": faker.name()}

    http_request = HttpRequest(query=attributes)

    http_response = find_user_adopter_route.route(http_request)
    # Testing input
    assert find_user_adopter_animal_shelter_case.by_user_information_param["name"] == attributes["name"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body



def test_route_error_400():
    """
    testing find user_adopter use case
    """

    find_user_adopter_animal_shelter_case = FindUserAdopterSpy(UserAdopterRepositorySpy())
    find_user_adopter_route = FindUserAdopterController(find_user_adopter_animal_shelter_case)

    attributes = {}

    http_request = HttpRequest(query=attributes)

    http_response = find_user_adopter_route.route(http_request)
    # Testing input
    assert not find_user_adopter_animal_shelter_case.by_user_adopter_id_param
    assert not find_user_adopter_animal_shelter_case.by_pet_id_param
    assert not find_user_adopter_animal_shelter_case.by_user_information_param

    # Testing output
    assert http_response.status_code == 400
    assert "error" in http_response.body



def test_route_error_422():
    """
    testing find user_adopter use case
    """

    find_user_adopter_animal_shelter_case = FindUserAdopterSpy(UserAdopterRepositorySpy())
    find_user_adopter_route = FindUserAdopterController(find_user_adopter_animal_shelter_case)

    attributes = {
        "id": faker.random_number(digits=5),
        "animal_id": faker.random_number(digits=5),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_user_adopter_route.route(http_request)
    # Testing input
    assert not find_user_adopter_animal_shelter_case.by_user_adopter_id_param
    assert not find_user_adopter_animal_shelter_case.by_pet_id_param
    assert not find_user_adopter_animal_shelter_case.by_user_information_param

    # Testing output
    assert http_response.status_code == 422
    assert "error" in http_response.body
