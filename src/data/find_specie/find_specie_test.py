from faker import Faker
from src.infra.test import SpecieRepositorySpy
from .find_specie import FindSpecie


faker = Faker()


def test_by_id():
    """
    Testing by_id method
    """

    specie_repo = SpecieRepositorySpy()
    find_specie = FindSpecie(specie_repo)

    attibutes = {
        "id": faker.random_number(digits=5),
    }

    response = find_specie.by_id(id=attibutes["id"])

    # Testing inputs
    assert specie_repo.select_specie_params["id"] == attibutes["id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """
    Testing by_id method
    """

    specie_repo = SpecieRepositorySpy()
    find_specie = FindSpecie(specie_repo)

    attibutes = {
        "id": faker.name(),
    }

    response = find_specie.by_id(id=attibutes["id"])

    # Testing inputs
    assert specie_repo.select_specie_params == {}  # pylint: disable=C1803

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_specie_name():
    """
    Testing by_specie_name method
    """

    specie_repo = SpecieRepositorySpy()
    find_specie = FindSpecie(specie_repo)

    attibutes = {
        "specie_name": faker.name(),
    }

    response = find_specie.by_specie_name(specie_name=attibutes["specie_name"])

    # Testing inputs
    assert specie_repo.select_specie_params["specie_name"] == attibutes["specie_name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_specie_name_fail():
    """
    Testing by_specie_name method
    """

    specie_repo = SpecieRepositorySpy()
    find_specie = FindSpecie(specie_repo)

    attibutes = {
        "specie_name": faker.random_number(digits=5),
    }

    response = find_specie.by_specie_name(specie_name=attibutes["specie_name"])

    # Testing inputs
    assert specie_repo.select_specie_params == {}  # pylint: disable=C1803

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_specie_name():
    """
    Testing by_id_and_specie_name method
    """

    specie_repo = SpecieRepositorySpy()
    find_specie = FindSpecie(specie_repo)

    attibutes = {
        "id": faker.random_number(digits=5),
        "specie_name": faker.name(),
    }

    response = find_specie.by_id_and_specie_name(id=attibutes["id"], specie_name=attibutes["specie_name"])

    # Testing inputs
    assert specie_repo.select_specie_params["id"] == attibutes["id"]
    assert specie_repo.select_specie_params["specie_name"] == attibutes["specie_name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_specie_name_fail():
    """
    Testing by_id_and_specie_name method
    """

    specie_repo = SpecieRepositorySpy()
    find_specie = FindSpecie(specie_repo)

    attibutes = {
        "id": faker.name(),
        "specie_name": faker.random_number(digits=5),
    }

    response = find_specie.by_id_and_specie_name(id=attibutes["id"], specie_name=attibutes["specie_name"])

    # Testing inputs
    assert specie_repo.select_specie_params == {}  # pylint: disable=C1803
    assert specie_repo.select_specie_params == {}  # pylint: disable=C1803

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
