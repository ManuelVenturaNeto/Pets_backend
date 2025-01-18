from faker import Faker
from src.infra.test import (
    UserAdopterRepositorySpy,
    AddressRepositorySpy,
    PetRepositorySpy,
)
from src.data.test import FindPetSpy
from src.data.register_address import RegisterAddress
from .register_user_adopter import RegisterUserAdopter


faker = Faker("pt_BR")


def test_register_user_adopter():
    """
    Testing register method
    """
    user_adopter_repo = UserAdopterRepositorySpy()
    address_repo = AddressRepositorySpy()
    register_address_service = RegisterAddress(address_repo)
    find_pet = FindPetSpy(PetRepositorySpy())
    register_user_adopter = RegisterUserAdopter(
        user_adopter_repo, find_pet, register_address_service
    )

    attributes = {
        "name": faker.name(),
        "cpf": faker.cpf().replace(".", "").replace("-", ""),
        "responsible_name": faker.name(),
        "email": faker.email(),
        "phone_number": str(faker.random_number(digits=11)).zfill(11),
        "pet_id": faker.random_number(digits=1),
        "cep": str(faker.random_number(digits=8)).zfill(8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.random_number(digits=3),
        "complement": faker.name(),
    }

    response = register_user_adopter.register_user_adopter(
        name=attributes["name"],
        cpf=attributes["cpf"],
        email=attributes["email"],
        phone_number=attributes["phone_number"],
        pet_id=attributes["pet_id"],
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
    assert (
        address_repo.insert_address_params["neighborhood"] == attributes["neighborhood"]
    )
    assert address_repo.insert_address_params["street"] == attributes["street"]
    assert address_repo.insert_address_params["number"] == attributes["number"]
    assert address_repo.insert_address_params["complement"] == attributes["complement"]

    # Testing inputs of find pet
    # assert address_repo.insert_address_params["pet_id"] == attributes["pet_id"]

    # Testing inputs of register_user_adopter
    assert user_adopter_repo.insert_user_adopter_params["name"] == attributes["name"]
    assert user_adopter_repo.insert_user_adopter_params["cpf"] == attributes["cpf"]
    assert user_adopter_repo.insert_user_adopter_params["email"] == attributes["email"]
    assert (
        user_adopter_repo.insert_user_adopter_params["phone_number"]
        == attributes["phone_number"]
    )
    # assert user_adopter_repo.insert_user_adopter_params["address_id"] == address_repo.insert_address_params["id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_user_adopter_fail():
    """
    Testing register method
    """
    user_adopter_repo = UserAdopterRepositorySpy()
    address_repo = AddressRepositorySpy()
    register_address_service = RegisterAddress(address_repo)
    find_pet = FindPetSpy(PetRepositorySpy())
    register_user_adopter = RegisterUserAdopter(
        user_adopter_repo, find_pet, register_address_service
    )

    attributes = {
        "name": faker.random_number(digits=3),
        "cpf": faker.name(),
        "email": faker.random_number(digits=3),
        "phone_number": faker.name(),
        "pet_id": faker.random_number(digits=1),
        "cep": str(faker.random_number(digits=8)).zfill(8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.random_number(digits=3),
        "complement": faker.name(),
    }

    response = register_user_adopter.register_user_adopter(
        name=attributes["name"],
        cpf=attributes["cpf"],
        email=attributes["email"],
        phone_number=attributes["phone_number"],
        pet_id=attributes["pet_id"],
        cep=attributes["cep"],
        state=attributes["state"],
        city=attributes["city"],
        neighborhood=attributes["neighborhood"],
        street=attributes["street"],
        number=attributes["number"],
        complement=attributes["complement"],
    )

    # Testing inputs
    assert not user_adopter_repo.insert_user_adopter_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_user_adopter_fail_address():
    """
    Testing register method
    """
    user_adopter_repo = UserAdopterRepositorySpy()
    address_repo = AddressRepositorySpy()
    register_address_service = RegisterAddress(address_repo)
    find_pet = FindPetSpy(PetRepositorySpy())
    register_user_adopter = RegisterUserAdopter(
        user_adopter_repo, find_pet, register_address_service
    )

    attributes = {
        "name": faker.name(),
        "cpf": faker.cpf().replace(".", "").replace("-", ""),
        "email": faker.email(),
        "phone_number": str(faker.random_number(digits=11)),
        "pet_id": faker.random_number(digits=1),
        "cep": faker.name(),
        "state": faker.random_number(digits=11),
        "city": faker.random_number(digits=11),
        "neighborhood": faker.random_number(digits=11),
        "street": faker.random_number(digits=11),
        "number": faker.random_number(digits=11),
        "complement": faker.name(),
    }

    response = register_user_adopter.register_user_adopter(
        name=attributes["name"],
        cpf=attributes["cpf"],
        email=attributes["email"],
        phone_number=attributes["phone_number"],
        pet_id=attributes["pet_id"],
        cep=attributes["cep"],
        state=attributes["state"],
        city=attributes["city"],
        neighborhood=attributes["neighborhood"],
        street=attributes["street"],
        number=attributes["number"],
        complement=attributes["complement"],
    )

    # Testing inputs
    assert not user_adopter_repo.insert_user_adopter_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_user_adopter_fail_pet_id():
    """
    Testing register method
    """
    user_adopter_repo = UserAdopterRepositorySpy()
    address_repo = AddressRepositorySpy()
    register_address_service = RegisterAddress(address_repo)
    find_pet = FindPetSpy(PetRepositorySpy())
    register_user_adopter = RegisterUserAdopter(
        user_adopter_repo, find_pet, register_address_service
    )

    attributes = {
        "name": faker.name(),
        "cpf": faker.cpf().replace(".", "").replace("-", ""),
        "responsible_name": faker.name(),
        "email": faker.email(),
        "phone_number": str(faker.random_number(digits=11)).zfill(11),
        "pet_id": faker.name(),
        "cep": str(faker.random_number(digits=8)).zfill(8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.random_number(digits=3),
        "complement": faker.name(),
    }

    response = register_user_adopter.register_user_adopter(
        name=attributes["name"],
        cpf=attributes["cpf"],
        email=attributes["email"],
        phone_number=attributes["phone_number"],
        pet_id=attributes["pet_id"],
        cep=attributes["cep"],
        state=attributes["state"],
        city=attributes["city"],
        neighborhood=attributes["neighborhood"],
        street=attributes["street"],
        number=attributes["number"],
        complement=attributes["complement"],
    )

    # Testing inputs
    assert not user_adopter_repo.insert_user_adopter_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
