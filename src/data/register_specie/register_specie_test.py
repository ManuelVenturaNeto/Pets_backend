from faker import Faker
from src.infra.test import SpecieRepositorySpy
from .register_specie import RegisterSpecie

faker = Faker()


def test_register_specie():
    """
    Testing register method
    """
    specie_repo = SpecieRepositorySpy()
    register_specie = RegisterSpecie(specie_repo)

    attributes = {
        "specie_name": faker.name(),
    }

    response = register_specie.register_specie(
        specie_name=attributes["specie_name"],
    )

    # Testing inputs
    assert specie_repo.insert_specie_params["specie_name"] == attributes["specie_name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_specie_fail():
    """
    Testing register method
    """
    specie_repo = SpecieRepositorySpy()
    register_specie = RegisterSpecie(specie_repo)

    attributes = {
        "specie_name": faker.random_number(digits=2),       
    }

    response = register_specie.register_specie(
        specie_name=attributes["specie_name"],

    )

    # Testing inputs
    assert specie_repo.insert_specie_params == {}  # pylint: disable=C1803

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
