from faker import Faker
from src.data.test import RegisterSpecieSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import SpecieRepositorySpy
from .register_specie_controller import RegisterSpecieController

faker = Faker("pt_BR")


def test_route():
    """
    Testing route method in RegisterSpecieController
    """

    register_specie_use_case = RegisterSpecieSpy(SpecieRepositorySpy())
    register_specie_router = RegisterSpecieController(register_specie_use_case)
    attributes = {"specie_name": faker.name()}

    response = register_specie_router.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_specie_use_case.register_param["specie_name"]
        == attributes["specie_name"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_400():
    """
    Testing route method in RegisterSpecieController
    """

    register_specie_use_case = RegisterSpecieSpy(SpecieRepositorySpy())
    register_specie_router = RegisterSpecieController(register_specie_use_case)

    response = register_specie_router.route(HttpRequest())

    # Testing input
    assert not register_specie_use_case.register_param

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_422():
    """
    Testing route method in RegisterSpecieController
    """

    register_specie_use_case = RegisterSpecieSpy(SpecieRepositorySpy())
    register_specie_router = RegisterSpecieController(register_specie_use_case)
    attributes = {"name": faker.name()}

    response = register_specie_router.route(HttpRequest(body=attributes))

    # Testing input
    assert not register_specie_use_case.register_param

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
