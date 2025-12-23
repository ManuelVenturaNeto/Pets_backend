from faker import Faker
from src.infra.test import UserAdopterRepositorySpy
from .find_user_adopter import FindUserAdopter


faker = Faker("pt_BR")


def test_by_user_adopter_id():
    """
    Testing by_user_adopter_id method
    """

    user_adopter_repo = UserAdopterRepositorySpy()
    find_user_adopter = FindUserAdopter(user_adopter_repo)

    attributes = {"user_adopter_id": faker.random_number(digits=5)}

    response = find_user_adopter.by_user_adopter_id(
        user_adopter_id=attributes["user_adopter_id"]
    )

    # testing input
    assert user_adopter_repo.select_user_adopter_params["id"] == attributes["user_adopter_id"]

    # testing output
    assert response["Success"] is True
    assert response["Data"]



def test_by_user_adopter_id_fail():
    """
    Testing by_user_adopter_id method
    """

    user_adopter_repo = UserAdopterRepositorySpy()
    find_user_adopter = FindUserAdopter(user_adopter_repo)

    attributes = {"user_adopter_id": faker.name()}

    response = find_user_adopter.by_user_adopter_id(user_adopter_id=attributes["user_adopter_id"])

    # testing input
    assert not user_adopter_repo.select_user_adopter_params

    # testing output
    assert response["Success"] is False
    assert response["Data"] is None



def test_by_pet_id():
    """
    Testing by_pet_id method
    """

    user_adopter_repo = UserAdopterRepositorySpy()
    find_user_adopter = FindUserAdopter(user_adopter_repo)

    attributes = {"pet_id": faker.random_number(digits=1)}

    response = find_user_adopter.by_pet_id(pet_id=attributes["pet_id"])

    # testing input
    assert user_adopter_repo.select_user_adopter_params["pet_id"] == attributes["pet_id"]

    # testing output
    assert response["Success"] is True
    assert response["Data"]



def test_by_pet_id_fail():
    """
    Testing by_pet_id method
    """

    user_adopter_repo = UserAdopterRepositorySpy()
    find_user_adopter = FindUserAdopter(user_adopter_repo)

    attributes = {"pet_id": faker.name()}

    response = find_user_adopter.by_pet_id(pet_id=attributes["pet_id"])

    # testing input
    assert not user_adopter_repo.select_user_adopter_params

    # testing output
    assert response["Success"] is False
    assert response["Data"] is None



def test_by_user_information():
    """
    Testing by_user_information method
    """

    user_adopter_repo = UserAdopterRepositorySpy()
    find_user_adopter = FindUserAdopter(user_adopter_repo)

    attributes = {
        "name": faker.name(),
        "cpf": faker.cpf().replace(".", "").replace("-", ""),
        "email": faker.email(),
        "phone_number": str(faker.random_number(digits=11)).zfill(11),
    }

    response = find_user_adopter.by_user_information(
        name=attributes["name"],
        cpf=attributes["cpf"],
        email=attributes["email"],
        phone_number=attributes["phone_number"],
    )

    # testing input
    assert user_adopter_repo.select_user_adopter_params["name"] == attributes["name"]
    assert user_adopter_repo.select_user_adopter_params["cpf"] == attributes["cpf"]
    assert user_adopter_repo.select_user_adopter_params["email"] == attributes["email"]
    assert user_adopter_repo.select_user_adopter_params["phone_number"] == attributes["phone_number"]

    # testing output
    assert response["Success"] is True
    assert response["Data"]



def test_by_user_information_fail():
    """
    Testing by_user_information method
    """

    user_adopter_repo = UserAdopterRepositorySpy()
    find_user_adopter = FindUserAdopter(user_adopter_repo)

    attributes = {"name": faker.random_number(digits=11)}

    response = find_user_adopter.by_user_information(name=attributes["name"])

    # testing input
    assert not user_adopter_repo.select_user_adopter_params
    assert not user_adopter_repo.select_user_adopter_params

    # testing output
    assert response["Success"] is False
    assert response["Data"] is None
