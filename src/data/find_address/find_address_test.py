from faker import Faker
from src.infra.test import AddressRepositorySpy
from .find_address import FindAddress


faker = Faker("pt_BR")


def test_by_id():
    """
    Testing by_id method
    """

    address_repo = AddressRepositorySpy()
    find_address = FindAddress(address_repo)

    attibutes = {
        "id": faker.random_number(digits=5),
    }

    response = find_address.by_id(id=attibutes["id"])

    # Testing inputs
    assert address_repo.select_address_params["id"] == attibutes["id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]



def test_by_id_fail():
    """
    Testing by_id method
    """

    address_repo = AddressRepositorySpy()
    find_address = FindAddress(address_repo)

    attibutes = {
        "id": faker.name(),
    }

    response = find_address.by_id(id=attibutes["id"])

    # Testing inputs
    assert not address_repo.select_address_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None



def test_by_complete_discription():
    """
    Testing by_complete_discription method
    """

    address_repo = AddressRepositorySpy()
    find_address = FindAddress(address_repo)

    attibutes = {
        "cep": str(faker.random_number(digits=8)).zfill(8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.random_number(digits=3),
    }

    response = find_address.by_complete_discription(
        cep=attibutes["cep"],
        state=attibutes["state"],
        city=attibutes["city"],
        neighborhood=attibutes["neighborhood"],
        street=attibutes["street"],
        number=attibutes["number"],
    )

    # Testing inputs
    assert address_repo.select_address_params["cep"] == attibutes["cep"]
    assert address_repo.select_address_params["state"] == attibutes["state"]
    assert address_repo.select_address_params["city"] == attibutes["city"]
    assert address_repo.select_address_params["neighborhood"] == attibutes["neighborhood"]
    assert address_repo.select_address_params["street"] == attibutes["street"]
    assert address_repo.select_address_params["number"] == attibutes["number"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]



def test_by_complete_discription_fail():
    """
    Testing by_complete_discription method
    """

    address_repo = AddressRepositorySpy()
    find_address = FindAddress(address_repo)

    attibutes = {
        "cep": faker.name(),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
        "street": faker.name(),
        "number": faker.name(),
    }

    response = find_address.by_complete_discription(
        cep=attibutes["cep"],
        state=attibutes["state"],
        city=attibutes["city"],
        neighborhood=attibutes["neighborhood"],
        street=attibutes["street"],
        number=attibutes["number"],
    )

    # Testing inputs
    assert not address_repo.select_address_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None



def test_by_cep_or_state_or_city_or_neighbohood():
    """
    Testing by_cep_or_state_or_city_or_neighbohood method
    """

    address_repo = AddressRepositorySpy()
    find_address = FindAddress(address_repo)

    attibutes = {
        "cep": str(faker.random_number(digits=8)).zfill(8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
    }

    response = find_address.by_cep_or_state_or_city_or_neighbohood(
        cep=attibutes["cep"],
        state=attibutes["state"],
        city=attibutes["city"],
        neighborhood=attibutes["neighborhood"],
    )

    # Testing inputs
    assert address_repo.select_address_params["cep"] == attibutes["cep"]
    assert address_repo.select_address_params["state"] == attibutes["state"]
    assert address_repo.select_address_params["city"] == attibutes["city"]
    assert address_repo.select_address_params["neighborhood"] == attibutes["neighborhood"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]



def test_by_cep_or_state_or_city_or_neighbohood_fail():
    """
    Testing by_cep_or_state_or_city_or_neighbohood method
    """

    address_repo = AddressRepositorySpy()
    find_address = FindAddress(address_repo)

    attibutes = {
        "cep": faker.random_number(digits=8),
        "state": faker.state_abbr(),
        "city": faker.name(),
        "neighborhood": faker.name(),
    }

    response = find_address.by_cep_or_state_or_city_or_neighbohood(cep=attibutes["cep"])

    # Testing inputs
    assert not address_repo.select_address_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
