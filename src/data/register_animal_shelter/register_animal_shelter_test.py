from unittest.mock import patch
import bcrypt
from faker import Faker
from src.infra.test import AnimalShelterRepositorySpy, AddressRepositorySpy
from .register_animal_shelter import RegisterAnimalShelter, RegisterAddress

faker = Faker("pt_BR")


def test_register_animal_shelter():
    """
    Testing register method
    """
    animal_shelter_repo = AnimalShelterRepositorySpy()
    address_repo = AddressRepositorySpy()
    register_address_service = RegisterAddress(address_repo)
    register_animal_shelter = RegisterAnimalShelter(
        animal_shelter_repo, register_address_service
    )

    attributes = {
        "name": faker.name(),
        "password": faker.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
        "cpf": faker.cpf().replace(".", "").replace("-", ""),
        "responsible_name": faker.name(),
        "email": faker.email(),
        "phone_number": str(faker.random_number(digits=11)).zfill(11),
        "cep": str(faker.random_number(digits=8)).zfill(8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.random_number(digits=3),
        "complement": faker.name(),
    }

    with patch("src.data.find_animal_shelter.FindAnimalShelter.by_name", return_value={"Data": None},), \
        patch("src.data.find_animal_shelter.FindAnimalShelter.by_cpf", return_value={"Data": None}):

        response = register_animal_shelter.register_animal_shelter(
            name=attributes["name"],
            password=attributes["password"],
            cpf=attributes["cpf"],
            responsible_name=attributes["responsible_name"],
            email=attributes["email"],
            phone_number=attributes["phone_number"],
            cep=attributes["cep"],
            state=attributes["state"],
            city=attributes["city"],
            neighborhood=attributes["neighborhood"],
            street=attributes["street"],
            number=attributes["number"],
            complement=attributes["complement"],
        )

    # Testing inputs of register_address_service

    assert address_repo.insert_address_params["cep"] == attributes["cep"]
    assert address_repo.insert_address_params["state"] == attributes["state"]
    assert address_repo.insert_address_params["city"] == attributes["city"]
    assert address_repo.insert_address_params["neighborhood"] == attributes["neighborhood"]
    assert address_repo.insert_address_params["street"] == attributes["street"]
    assert address_repo.insert_address_params["number"] == attributes["number"]
    assert address_repo.insert_address_params["complement"] == attributes["complement"]

    # Testing inputs of register_animal_shelter
    assert animal_shelter_repo.insert_animal_shelter_params["name"] == attributes["name"]
    assert bcrypt.checkpw(attributes["password"].encode("utf-8"), animal_shelter_repo.insert_animal_shelter_params["password"])
    assert animal_shelter_repo.insert_animal_shelter_params["cpf"] == attributes["cpf"]
    assert animal_shelter_repo.insert_animal_shelter_params["responsible_name"] == attributes["responsible_name"]
    assert animal_shelter_repo.insert_animal_shelter_params["email"] == attributes["email"]
    assert animal_shelter_repo.insert_animal_shelter_params["phone_number"] == attributes["phone_number"]
    # assert animal_shelter_repo.insert_animal_shelter_params["address_id"] == address_repo.insert_address_params["id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_animal_shelter_fail():
    """
    Testing register method
    """
    animal_shelter_repo = AnimalShelterRepositorySpy()
    address_repo = AddressRepositorySpy()
    register_address_service = RegisterAddress(address_repo)
    register_animal_shelter = RegisterAnimalShelter(
        animal_shelter_repo, register_address_service
    )

    attributes = {
        "name": faker.random_number(digits=3),
        "password": faker.random_number(digits=3),
        "cpf": faker.random_number(digits=11),
        "responsible_name": faker.random_number(digits=3),
        "email": faker.random_number(digits=3),
        "phone_number": faker.random_number(digits=11),
        "cep": str(faker.random_number(digits=8)).zfill(8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.random_number(digits=3),
        "complement": faker.name(),
    }

    with patch("src.data.find_animal_shelter.FindAnimalShelter.by_name", return_value={"Data": None}), \
        patch("src.data.find_animal_shelter.FindAnimalShelter.by_cpf", return_value={"Data": None}):

        response = register_animal_shelter.register_animal_shelter(
            name=attributes["name"],
            password=attributes["password"],
            cpf=attributes["cpf"],
            responsible_name=attributes["responsible_name"],
            email=attributes["email"],
            phone_number=attributes["phone_number"],
            cep=attributes["cep"],
            state=attributes["state"],
            city=attributes["city"],
            neighborhood=attributes["neighborhood"],
            street=attributes["street"],
            number=attributes["number"],
            complement=attributes["complement"],
        )

    # Testing inputs
    assert not animal_shelter_repo.insert_animal_shelter_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None



def test_register_animal_shelter_fail_address():
    """
    Testing register method
    """
    animal_shelter_repo = AnimalShelterRepositorySpy()
    address_repo = AddressRepositorySpy()
    register_address_service = RegisterAddress(address_repo)
    register_animal_shelter = RegisterAnimalShelter(animal_shelter_repo, register_address_service)

    attributes = {
        "name": faker.name(),
        "password": faker.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
        "cpf": faker.cpf().replace(".", "").replace("-", ""),
        "responsible_name": faker.name(),
        "email": faker.email(),
        "phone_number": str(faker.random_number(digits=11)).zfill(11),
        "cep": faker.random_number(digits=8),
        "state": faker.random_number(digits=11),
        "city": faker.random_number(digits=11),
        "neighborhood": faker.random_number(digits=11),
        "street": faker.random_number(digits=11),
        "number": faker.random_number(digits=11),
        "complement": faker.name(),
    }

    with patch("src.data.find_animal_shelter.FindAnimalShelter.by_name", return_value={"Data": None}), \
        patch("src.data.find_animal_shelter.FindAnimalShelter.by_cpf", return_value={"Data": None}):

        response = register_animal_shelter.register_animal_shelter(
            name=attributes["name"],
            password=attributes["password"],
            cpf=attributes["cpf"],
            responsible_name=attributes["responsible_name"],
            email=attributes["email"],
            phone_number=attributes["phone_number"],
            cep=attributes["cep"],
            state=attributes["state"],
            city=attributes["city"],
            neighborhood=attributes["neighborhood"],
            street=attributes["street"],
            number=attributes["number"],
            complement=attributes["complement"],
        )

    # Testing inputs
    assert not animal_shelter_repo.insert_animal_shelter_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
