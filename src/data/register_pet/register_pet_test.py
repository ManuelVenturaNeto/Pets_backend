from faker import Faker
from src.infra.test import AnimalShelterRepositorySpy, PetRepositorySpy, SpecieRepositorySpy
from src.data.test import FindAnimalShelterSpy, FindSpecieSpy
from .register_pet import RegisterPet

faker = Faker()


def test_register_pet():
    """
    Testing register method in RegisterPet
    """

    pet_repo = PetRepositorySpy()
    find_animal_shelter = FindAnimalShelterSpy(AnimalShelterRepositorySpy())
    find_specie = FindSpecieSpy(SpecieRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_animal_shelter, find_specie)

    attributes = {
        "name": faker.name(),
        "specie_name": "Dog",
        "age": faker.random_number(digits=2),
        "animal_shelter_information": {
            "animal_shelter_id": faker.random_number(digits=5),
            "animal_shelter_name": faker.name(),
        },
        "adopted": False,
    }

    response = register_pet.register_pet(
        name=attributes["name"],
        specie_name=attributes["specie_name"],
        animal_shelter_information=attributes["animal_shelter_information"],
        adopted=attributes["adopted"],
        age=attributes["age"],
    )

    print("Captured Params in PetRepo:", pet_repo.insert_pet_param)
    print("Captured Params in FindAnimalShelter:", find_animal_shelter.by_id_and_name_param)
    print("Response:", response)

    # testing inputs
    assert pet_repo.insert_pet_param["name"] == attributes["name"]
    # assert pet_repo.insert_pet_param["specie"] == attributes["specie_name"]
    assert pet_repo.insert_pet_param["age"] == attributes["age"]

    # testing FindAnimalShelter inputs
    assert (
        find_animal_shelter.by_id_and_name_param["animal_shelter_id"]
        == attributes["animal_shelter_information"]["animal_shelter_id"]
    )
    assert (
        find_animal_shelter.by_id_and_name_param["name"]
        == attributes["animal_shelter_information"]["animal_shelter_name"]
    )

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_pet_fail():
    """
    Testing register method in RegisterPet
    """

    pet_repo = PetRepositorySpy()
    find_animal_shelter = FindAnimalShelterSpy(AnimalShelterRepositorySpy())
    find_specie = FindSpecieSpy(SpecieRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_animal_shelter, find_specie)

    attributes = {
        "name": faker.random_number(digits=2),
        "specie_name": faker.name(),
        "age": faker.name(),
        "animal_shelter_information": {
            "animal_shelter_id": faker.random_number(digits=5),
            "animal_shelter_name": faker.name(),
        },
        "adopted": False,
    }

    response = register_pet.register_pet(
        name=attributes["name"],
        specie_name=attributes["specie_name"],
        animal_shelter_information=attributes["animal_shelter_information"],
        adopted=attributes["adopted"],
        age=attributes["age"],
    )

    # testing inputs
    assert pet_repo.insert_pet_param == {}  # pylint: disable=C1803
    assert pet_repo.insert_pet_param == {}  # pylint: disable=C1803
    assert pet_repo.insert_pet_param == {}  # pylint: disable=C1803

    # testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
