from faker import Faker
from src.data.test import RegisterPetSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import (
    PetRepositorySpy,
    AnimalShelterRepositorySpy,
    SpecieRepositorySpy,
)
from .register_pet_controller import RegisterPetController

faker = Faker("pt_BR")


def test_route():
    """
    Testing route method in RegisterAnimalShelterroute
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), AnimalShelterRepositorySpy(), SpecieRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "specie_name": "Dog",
        "age": faker.random_number(digits=2),
        "animal_shelter_information": {
            "animal_shelter_id": faker.random_number(digits=5),
            "animal_shelter_name": faker.name(),
        },
        "adopted": False,
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param["name"] == attributes["name"]
    assert register_pet_use_case.register_pet_param["specie_name"] == attributes["specie_name"]
    assert register_pet_use_case.register_pet_param["age"] == attributes["age"]
    assert register_pet_use_case.register_pet_param["animal_shelter_information"] == attributes["animal_shelter_information"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body



def test_route_without_age():
    """
    Testing route method in RegisterAnimalShelterrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), AnimalShelterRepositorySpy(), SpecieRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "specie_name": "Dog",
        "animal_shelter_information": {
            "animal_shelter_id": faker.random_number(digits=5),
            "animal_shelter_name": faker.name(),
        },
        "adopted": False,
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param["name"] == attributes["name"]
    assert register_pet_use_case.register_pet_param["specie_name"] == attributes["specie_name"]
    assert register_pet_use_case.register_pet_param["age"] is None
    assert register_pet_use_case.register_pet_param["animal_shelter_information"] == attributes["animal_shelter_information"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body



def test_route_animal_shelter_id_in_animal_shelter_information():
    """
    Testing route method in RegisterAnimalShelterrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), AnimalShelterRepositorySpy(), SpecieRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "specie_name": "Dog",
        "animal_shelter_information": {"animal_shelter_name": faker.name()},
        "adopted": False,
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.register_pet_param["name"] == attributes["name"]
    assert register_pet_use_case.register_pet_param["specie_name"] == attributes["specie_name"]
    assert register_pet_use_case.register_pet_param["age"] is None
    assert register_pet_use_case.register_pet_param["animal_shelter_information"] == attributes["animal_shelter_information"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body



def test_route_error_400():
    """
    Testing route method in RegisterAnimalShelterrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), AnimalShelterRepositorySpy(), SpecieRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    response = register_pet_router.route(HttpRequest())

    # Testing input
    assert not register_pet_use_case.register_pet_param

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body



def test_route_error_422_wrong_body():
    """
    Testing route method in RegisterAnimalShelterrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), AnimalShelterRepositorySpy(), SpecieRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "specie": "Dog",
        "animal_shelter_information": {
            "animal_shelter_id": faker.random_number(),
            "animal_shelter_name": faker.name(),
        },
        "adopted": False,
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert not register_pet_use_case.register_pet_param

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body



def test_route_error_422_wrong_animal_shelter_information():
    """
    Testing route method in RegisterAnimalShelterrouter
    """

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), AnimalShelterRepositorySpy(), SpecieRepositorySpy())
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "specie": "Dog",
        "animal_shelter_information": {},
        "adopted": False,
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert not register_pet_use_case.register_pet_param

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
