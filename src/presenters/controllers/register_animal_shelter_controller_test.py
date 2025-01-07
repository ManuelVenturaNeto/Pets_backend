from faker import Faker
from src.data.test import RegisterAnimalShelterSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import AnimalShelterRepositorySpy, AddressRepositorySpy
from .register_animal_shelter_controller import RegisterAnimalShelterController

faker = Faker()


def test_route():
    """
    Testing route method in RegisterAnimalShelterController
    """

    register_animal_shelter_use_case = RegisterAnimalShelterSpy(AnimalShelterRepositorySpy(), AddressRepositorySpy())
    register_animal_shelter_router = RegisterAnimalShelterController(register_animal_shelter_use_case)
    attributes = {  "name": faker.name(),
                    "password": faker.password(),
                    "cpf": faker.random_number(digits=11),
                    "responsible_name": faker.name(),
                    "email": faker.email(),
                    "phone_number": faker.random_number(digits=11),
                    "cep": faker.random_number(digits=8),
                    "state": faker.state_abbr(),
                    "city": faker.name(),
                    "neighborhood": faker.name(),
                    "street": faker.name(),
                    "number": faker.random_number(digits=3),
                    "complement": faker.name(),
                    }

    response = register_animal_shelter_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_animal_shelter_use_case.register_param["name"] == attributes["name"]
    assert register_animal_shelter_use_case.register_param["password"] == attributes["password"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_400():
    """
    Testing route method in RegisterAnimalShelterController
    """

    register_animal_shelter_use_case = RegisterAnimalShelterSpy(AnimalShelterRepositorySpy(), AddressRepositorySpy())
    register_animal_shelter_router = RegisterAnimalShelterController(register_animal_shelter_use_case)

    response = register_animal_shelter_router.route(HttpRequest())

    # Testing input
    assert register_animal_shelter_use_case.register_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_422():
    """
    Testing route method in RegisterAnimalShelterController
    """

    register_animal_shelter_use_case = RegisterAnimalShelterSpy(AnimalShelterRepositorySpy(), AddressRepositorySpy())
    register_animal_shelter_router = RegisterAnimalShelterController(register_animal_shelter_use_case)
    attributes = {"name": faker.name()}

    response = register_animal_shelter_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_animal_shelter_use_case.register_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
