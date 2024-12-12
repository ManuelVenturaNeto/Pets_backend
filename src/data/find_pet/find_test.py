from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet


faker = Faker()


def test_by_pet_id():
    """
    Testing by_pet_id method
    """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=5)}

    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # testing input
    assert pet_repo.select_pet_param["pet_id"] == attributes["pet_id"]

    # testing output
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_fail():
    """
    Testing by_pet_id method
    """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.name()}

    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # testing input
    assert pet_repo.select_pet_param == {}  # pylint: disable=C1803

    # testing output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_user_id():
    """
    Testing by_user_id method
    """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.random_number(digits=5)}

    response = find_pet.by_user_id(user_id=attributes["user_id"])

    # testing input
    assert pet_repo.select_pet_param["user_id"] == attributes["user_id"]

    # testing output
    assert response["Success"] is True
    assert response["Data"]


def test_by_user_id__fail():
    """
    Testing by_user_id method
    """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.name()}

    response = find_pet.by_user_id(user_id=attributes["user_id"])

    # testing input
    assert pet_repo.select_pet_param == {}  # pylint: disable=C1803

    # testing output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_pet_id_and_user_id():
    """
    Testing by_pet_id_and_user_id method
    """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "pet_id": faker.random_number(digits=5),
        "user_id": faker.random_number(digits=5),
    }

    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], user_id=attributes["user_id"]
    )

    # testing input
    assert pet_repo.select_pet_param["pet_id"] == attributes["pet_id"]
    assert pet_repo.select_pet_param["user_id"] == attributes["user_id"]

    # testing output
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_and_user_id_fail():
    """
    Testing by_pet_id_and_user_id method
    """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "pet_id": faker.name(),
        "user_id": faker.name(),
    }

    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], user_id=attributes["user_id"]
    )

    # testing input
    assert pet_repo.select_pet_param == {}  # pylint: disable=C1803
    assert pet_repo.select_pet_param == {}  # pylint: disable=C1803

    # testing output
    assert response["Success"] is False
    assert response["Data"] is None
