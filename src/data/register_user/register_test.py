import bcrypt
from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register_user():
    """
    Testing register method
    """
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.name(),
        "password": faker.password(),
    }

    response = register_user.register_user(
        name=attributes["name"],
        password=attributes["password"],
    )

    # Testing inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert bcrypt.checkpw(
        attributes["password"].encode("utf-8"), user_repo.insert_user_params["password"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_user_fail():
    """
    Testing register method
    """
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.random_number(digits=5),
        "password": faker.password(),
    }

    response = register_user.register_user(
        name=attributes["name"],
        password=attributes["password"],
    )

    # Testing inputs
    assert user_repo.insert_user_params == {}  # pylint: disable=C1803

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
