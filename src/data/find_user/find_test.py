from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser


faker = Faker()


def test_by_id():
    """
    Testing by_id method
    """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attibutes = {
        "id": faker.random_number(digits=5),
    }

    response = find_user.by_id(user_id=attibutes["id"])

    # Testing inputs
    assert user_repo.select_user_params["user_id"] == attibutes["id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """
    Testing by_id method
    """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attibutes = {
        "id": faker.name(),
    }

    response = find_user.by_id(user_id=attibutes["id"])

    # Testing inputs
    assert user_repo.select_user_params == {}  # pylint: disable=C1803

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """
    Testing by_name method
    """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attibutes = {
        "name": faker.name(),
    }

    response = find_user.by_name(name=attibutes["name"])

    # Testing inputs
    assert user_repo.select_user_params["name"] == attibutes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_name_fail():
    """
    Testing by_name method
    """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attibutes = {
        "name": faker.random_number(digits=5),
    }

    response = find_user.by_name(name=attibutes["name"])

    # Testing inputs
    assert user_repo.select_user_params == {}  # pylint: disable=C1803

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name():
    """
    Testing by_id_and_name method
    """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attibutes = {
        "id": faker.random_number(digits=5),
        "name": faker.name(),
    }

    response = find_user.by_id_and_name(user_id=attibutes["id"], name=attibutes["name"])

    # Testing inputs
    assert user_repo.select_user_params["user_id"] == attibutes["id"]
    assert user_repo.select_user_params["name"] == attibutes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_name_fail():
    """
    Testing by_id_and_name method
    """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attibutes = {
        "id": faker.name(),
        "name": faker.random_number(digits=5),
    }

    response = find_user.by_id_and_name(user_id=attibutes["id"], name=attibutes["name"])

    # Testing inputs
    assert user_repo.select_user_params == {}  # pylint: disable=C1803
    assert user_repo.select_user_params == {}  # pylint: disable=C1803

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
