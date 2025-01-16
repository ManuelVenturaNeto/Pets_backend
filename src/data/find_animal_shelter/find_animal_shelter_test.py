from faker import Faker
from src.infra.test import AnimalShelterRepositorySpy
from .find_animal_shelter import FindAnimalShelter


faker = Faker()


def test_by_id():
    """
    Testing by_id method
    """

    animal_shelter_repo = AnimalShelterRepositorySpy()
    find_animal_shelter = FindAnimalShelter(animal_shelter_repo)

    attibutes = {
        "id": faker.random_number(digits=5),
    }

    response = find_animal_shelter.by_id(id=attibutes["id"])

    # Testing inputs
    assert animal_shelter_repo.select_animal_shelter_params["id"] == attibutes["id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """
    Testing by_id method
    """

    animal_shelter_repo = AnimalShelterRepositorySpy()
    find_animal_shelter = FindAnimalShelter(animal_shelter_repo)

    attibutes = {
        "id": faker.name(),
    }

    response = find_animal_shelter.by_id(id=attibutes["id"])

    # Testing inputs
    assert not animal_shelter_repo.select_animal_shelter_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """
    Testing by_name method
    """

    animal_shelter_repo = AnimalShelterRepositorySpy()
    find_animal_shelter = FindAnimalShelter(animal_shelter_repo)

    attibutes = {
        "name": faker.name(),
    }

    response = find_animal_shelter.by_name(name=attibutes["name"])

    # Testing inputs
    assert animal_shelter_repo.select_animal_shelter_params["name"] == attibutes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_name_fail():
    """
    Testing by_name method
    """

    animal_shelter_repo = AnimalShelterRepositorySpy()
    find_animal_shelter = FindAnimalShelter(animal_shelter_repo)

    attibutes = {
        "name": faker.random_number(digits=5),
    }

    response = find_animal_shelter.by_name(name=attibutes["name"])

    # Testing inputs
    assert not animal_shelter_repo.select_animal_shelter_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name():
    """
    Testing by_id_and_name method
    """

    animal_shelter_repo = AnimalShelterRepositorySpy()
    find_animal_shelter = FindAnimalShelter(animal_shelter_repo)

    attibutes = {
        "id": faker.random_number(digits=5),
        "name": faker.name(),
    }

    response = find_animal_shelter.by_id_and_name(
        id=attibutes["id"], name=attibutes["name"]
    )

    # Testing inputs
    assert animal_shelter_repo.select_animal_shelter_params["id"] == attibutes["id"]
    assert animal_shelter_repo.select_animal_shelter_params["name"] == attibutes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_name_fail():
    """
    Testing by_id_and_name method
    """

    animal_shelter_repo = AnimalShelterRepositorySpy()
    find_animal_shelter = FindAnimalShelter(animal_shelter_repo)

    attibutes = {
        "id": faker.name(),
        "name": faker.random_number(digits=5),
    }

    response = find_animal_shelter.by_id_and_name(
        id=attibutes["id"], name=attibutes["name"]
    )

    # Testing inputs
    assert not animal_shelter_repo.select_animal_shelter_params
    assert not animal_shelter_repo.select_animal_shelter_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
