from faker import Faker
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController

faker = Faker()


def test_route():
    """
    testing route method
    """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(
        query={"user_id": faker.random_number(digits=5), "user_name": faker.name()}
    )

    response = find_user_controller.route(http_request)

    # testing inputs
    assert (
        find_user_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )

    # testing outputs
    assert response.status_code == 200
    assert response.body


def test_route_error_400():
    """
    testing route method
    """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.route(http_request)

    # testing inputs
    assert find_user_use_case.by_id_and_name_param == {}  # pylint: disable=C1803
    assert find_user_use_case.by_id_param == {}  # pylint: disable=C1803
    assert find_user_use_case.by_name_param == {}  # pylint: disable=C1803

    # testing outputs
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_422():
    """
    testing route method
    """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(
        query={
            "invalid_entry": faker.random_number(digits=5),
            "other_invalidy_entry": faker.name(),
        }
    )

    response = find_user_controller.route(http_request)

    # testing inputs
    assert find_user_use_case.by_id_and_name_param == {}  # pylint: disable=C1803
    assert find_user_use_case.by_id_param == {}  # pylint: disable=C1803
    assert find_user_use_case.by_name_param == {}  # pylint: disable=C1803

    # testing outputs
    assert response.status_code == 422
    assert "error" in response.body
