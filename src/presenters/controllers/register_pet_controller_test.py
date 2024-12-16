from faker import Faker
from src.infra.entities.pets import AnimalTypes
from src.data.test import RegisterPetSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from .register_pet_controller import RegisterPetController

faker = Faker()


def test_route():
    """
    Testing route method in RegisterUserroute
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)
    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name(),
        },
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param["name"] == attributes["name"]
    assert register_pet_use_case.register_pet_param["species"] == attributes["species"]
    assert register_pet_use_case.register_pet_param["age"] == attributes["age"]
    assert (
        register_pet_use_case.register_pet_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_without_age():
    """
    Testing route method in RegisterUserrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)
    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name(),
        },
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param["name"] == attributes["name"]
    assert register_pet_use_case.register_pet_param["species"] == attributes["species"]
    assert register_pet_use_case.register_pet_param["age"] is None
    assert (
        register_pet_use_case.register_pet_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_user_id_in_user_information():
    """
    Testing route method in RegisterUserrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "user_information": {"user_name": faker.name()},
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param["name"] == attributes["name"]
    assert register_pet_use_case.register_pet_param["species"] == attributes["species"]
    assert register_pet_use_case.register_pet_param["age"] is None
    assert (
        register_pet_use_case.register_pet_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_400():
    """
    Testing route method in RegisterUserrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    response = register_pet_router.route(HttpRequest())

    # Testing input
    assert register_pet_use_case.register_pet_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_422_wrong_body():
    """
    Testing route method in RegisterUserrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "species": faker.enum(AnimalTypes).name,
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name(),
        },
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_route_error_422_wrong_user_information():
    """
    Testing route method in RegisterUserrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "user_information": {},
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
