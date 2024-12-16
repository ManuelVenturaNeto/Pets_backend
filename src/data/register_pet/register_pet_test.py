from faker import Faker
from src.infra.entities.pets import AnimalTypes
from src.infra.test import UserRepositorySpy, PetRepositorySpy
from src.data.test import FindUserSpy
from .register_pet import RegisterPet

faker = Faker()


def test_register_pet():
    """
    Testing register method in RegisterPet
    """

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "species": faker.enum(AnimalTypes).name,
        "age": faker.random_number(digits=2),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }

    response = register_pet.register_pet(
        attributes["name"],
        attributes["species"],
        attributes["user_information"],
        attributes["age"],
    )

    # testing inputs
    assert pet_repo.insert_pet_param["name"] == attributes["name"]
    assert pet_repo.insert_pet_param["species"] == attributes["species"]
    assert pet_repo.insert_pet_param["age"] == attributes["age"]

    # testing FindUser inputs
    assert (
        find_user.by_id_and_name_param["user_id"]
        == attributes["user_information"]["user_id"]
    )
    assert (
        find_user.by_id_and_name_param["name"]
        == attributes["user_information"]["user_name"]
    )

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_pet_fail():
    """
    Testing register method in RegisterPet
    """

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.random_number(digits=2),
        "species": faker.random_number(digits=2),
        "age": faker.name(),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }

    response = register_pet.register_pet(
        attributes["name"],
        attributes["species"],
        attributes["user_information"],
        attributes["age"],
    )

    # testing inputs
    assert pet_repo.insert_pet_param == {}  # pylint: disable=C1803
    assert pet_repo.insert_pet_param == {}  # pylint: disable=C1803
    assert pet_repo.insert_pet_param == {}  # pylint: disable=C1803

    # testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
