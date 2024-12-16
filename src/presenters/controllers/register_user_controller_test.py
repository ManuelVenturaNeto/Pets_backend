from faker import Faker
from src.data.test import RegisterUserSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import UserRepositorySpy
from .register_user_controller import RegisterUserController

faker = Faker()


def test_route():
    """
    Testing route method in RegisterUserController
    """

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_router = RegisterUserController(register_user_use_case)
    attributes = {"name": faker.name(), "password": faker.password()}

    response = register_user_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_user_use_case.register_param["name"] == attributes["name"]
    assert register_user_use_case.register_param["password"] == attributes["password"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_400():
    """
    Testing route method in RegisterUserController
    """

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_router = RegisterUserController(register_user_use_case)

    response = register_user_router.route(HttpRequest())

    # Testing input
    assert register_user_use_case.register_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_422():
    """
    Testing route method in RegisterUserController
    """

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_router = RegisterUserController(register_user_use_case)
    attributes = {"name": faker.name()}

    response = register_user_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_user_use_case.register_param == {}  # pylint: disable=C1803

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
