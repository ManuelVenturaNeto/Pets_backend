from faker import Faker
from src.infra.entities.pets import AnimalTypes
from src.data.test import RegisterPetSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from .register_pet_controller import RegisterPetController

faker = Faker()


def test_handle():
    """Testing handle method in RegisterUserHandle"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_handler = RegisterPetController(register_pet_use_case)
    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name(),
        },
    }

    response = register_pet_handler.handle(HttpRequest(body=attributes))

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


def test_handle_without_age():
    """Testing handle method in RegisterUserhandler"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_handler = RegisterPetController(register_pet_use_case)
    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name(),
        },
    }

    response = register_pet_handler.handle(HttpRequest(body=attributes))

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


def test_handle_user_id_in_user_information():
    """Testing handle method in RegisterUserhandler"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_handler = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "user_information": {"user_name": faker.name()},
    }

    response = register_pet_handler.handle(HttpRequest(body=attributes))

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


def test_handle_error_no_body():
    """Testing handle method in RegisterUserhandler"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_handler = RegisterPetController(register_pet_use_case)

    response = register_pet_handler.handle(HttpRequest())

    # Testing input
    assert register_pet_use_case.register_pet_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_handle_error_wrong_body():
    """Testing handle method in RegisterUserhandler"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_handler = RegisterPetController(register_pet_use_case)

    attributes = {
        "species": faker.enum(AnimalTypes).name,
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name(),
        },
    }

    response = register_pet_handler.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_error_wrong_user_information():
    """Testing handle method in RegisterUserhandler"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_handler = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "user_information": {},
    }

    response = register_pet_handler.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
