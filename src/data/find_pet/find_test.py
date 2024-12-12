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
