from faker import Faker
from src.infra.test import AddressRepositorySpy
from .register_address import RegisterAddress

faker = Faker("pt_BR")


def test_register_address():
    """
    Testing register method
    """
    address_repo = AddressRepositorySpy()
    register_address = RegisterAddress(address_repo)

    attributes = {
        "cep": faker.random_number(digits=8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.random_number(digits=3),
        "complement": faker.name(),
    }

    response = register_address.register_address(
        cep=attributes["cep"],
        state=attributes["state"],
        city=attributes["city"],
        neighborhood=attributes["neighborhood"],
        street=attributes["street"],
        number=attributes["number"],
        complement=attributes["complement"],
    )

    # Testing inputs
    assert address_repo.insert_address_params["cep"] == attributes["cep"]
    assert address_repo.insert_address_params["state"] == attributes["state"]
    assert address_repo.insert_address_params["city"] == attributes["city"]
    assert (
        address_repo.insert_address_params["neighborhood"] == attributes["neighborhood"]
    )
    assert address_repo.insert_address_params["street"] == attributes["street"]
    assert address_repo.insert_address_params["number"] == attributes["number"]
    assert address_repo.insert_address_params["complement"] == attributes["complement"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_address_fail():
    """
    Testing register method
    """
    address_repo = AddressRepositorySpy()
    register_address = RegisterAddress(address_repo)

    attributes = {
        "cep": faker.state_abbr(),
        "state": faker.random_number(digits=3),
        "city": faker.random_number(digits=3),
        "neighborhood": faker.random_number(digits=3),
        "street": faker.random_number(digits=3),
        "number": faker.state_abbr(),
        "complement": faker.random_number(digits=3),
    }

    response = register_address.register_address(
        cep=attributes["cep"],
        state=attributes["state"],
        city=attributes["city"],
        neighborhood=attributes["neighborhood"],
        street=attributes["street"],
        number=attributes["number"],
        complement=attributes["complement"],
    )

    # Testing inputs
    assert not address_repo.insert_address_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
