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
