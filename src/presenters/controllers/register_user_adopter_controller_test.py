from faker import Faker
from src.data.test import RegisterUserAdopterSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import UserAdopterRepositorySpy, AddressRepositorySpy
from .register_user_adopter_controller import RegisterUserAdopterController

faker = Faker("pt_BR")


def test_route():
    """
    Testing route method in RegisterUserAdopterController
    """

    register_user_adopter_use_case = RegisterUserAdopterSpy(UserAdopterRepositorySpy(), AddressRepositorySpy())
    register_user_adopter_router = RegisterUserAdopterController(register_user_adopter_use_case)

    attributes = {
        "name": faker.name(),
        "cpf": faker.cpf().replace(".", "").replace("-", ""),
        "email": faker.email(),
        "phone_number": str(faker.random_number(digits=11)).zfill(11),
        "pet_id": faker.random_number(digits=1),
        "cep": str(faker.random_number(digits=8)).zfill(8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.random_number(digits=3),
        "complement": faker.name(),
    }

    response = register_user_adopter_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_user_adopter_use_case.register_param["name"] == attributes["name"]
    assert register_user_adopter_use_case.register_param["cpf"] == attributes["cpf"]
    assert register_user_adopter_use_case.register_param["email"] == attributes["email"]
    assert register_user_adopter_use_case.register_param["phone_number"] == attributes["phone_number"]
    assert register_user_adopter_use_case.register_param["pet_id"] == attributes["pet_id"]
    assert register_user_adopter_use_case.register_param["cep"] == attributes["cep"]
    assert register_user_adopter_use_case.register_param["state"] == attributes["state"]
    assert register_user_adopter_use_case.register_param["city"] == attributes["city"]
    assert register_user_adopter_use_case.register_param["neighborhood"] == attributes["neighborhood"]
    assert register_user_adopter_use_case.register_param["street"] == attributes["street"]
    assert register_user_adopter_use_case.register_param["number"] == attributes["number"]
    assert register_user_adopter_use_case.register_param["complement"] == attributes["complement"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body



def test_route_error_400():
    """
    Testing route method in RegisterUserAdopterController
    """

    register_user_adopter_use_case = RegisterUserAdopterSpy(UserAdopterRepositorySpy(), AddressRepositorySpy())
    register_user_adopter_router = RegisterUserAdopterController(register_user_adopter_use_case)

    response = register_user_adopter_router.route(HttpRequest())

    # Testing input
    assert not register_user_adopter_use_case.register_param

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body



def test_route_error_422():
    """
    Testing route method in RegisterUserAdopterController
    """

    register_user_adopter_use_case = RegisterUserAdopterSpy(UserAdopterRepositorySpy(), AddressRepositorySpy())
    register_user_adopter_router = RegisterUserAdopterController(register_user_adopter_use_case)
    attributes = {"name": faker.name()}

    response = register_user_adopter_router.route(HttpRequest(body=attributes))

    # Testing input
    assert not register_user_adopter_use_case.register_param

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
