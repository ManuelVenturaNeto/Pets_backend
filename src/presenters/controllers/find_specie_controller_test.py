from faker import Faker
from src.data.test import FindSpecieSpy
from src.infra.test import SpecieRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_specie_controller import FindSpecieController

faker = Faker("pt_BR")


def test_route():
    """
    testing find specie use case
    """

    find_specie_specie_case = FindSpecieSpy(SpecieRepositorySpy())
    find_specie_route = FindSpecieController(find_specie_specie_case)

    attributes = {
        "id": 1,
        "specie_name": "Dog",
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_specie_route.route(http_request)
    # Testing input
    assert find_specie_specie_case.by_id_and_specie_name_param["specie_name"] == attributes["specie_name"]
    assert find_specie_specie_case.by_id_and_specie_name_param["specie_name"] == attributes["specie_name"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body



def test_route_error_400():
    """
    testing find specie use case
    """

    find_specie_specie_case = FindSpecieSpy(SpecieRepositorySpy())
    find_specie_route = FindSpecieController(find_specie_specie_case)

    attributes = {}

    http_request = HttpRequest(query=attributes)

    http_response = find_specie_route.route(http_request)

    # Testing input
    assert not find_specie_specie_case.by_id_and_specie_name_param

    # Testing output
    assert http_response.status_code == 400
    assert "error" in http_response.body



def test_route_error_422():
    """
    testing find specie use case
    """

    find_specie_specie_case = FindSpecieSpy(SpecieRepositorySpy())
    find_specie_route = FindSpecieController(find_specie_specie_case)

    attributes = {
        "pet_id": 1,
        "name": "Dog",
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_specie_route.route(http_request)
    # Testing input
    assert not find_specie_specie_case.by_id_and_specie_name_param

    # Testing output
    assert http_response.status_code == 422
    assert "error" in http_response.body
