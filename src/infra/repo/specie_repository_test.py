import pytest
from sqlalchemy import text
from faker import Faker
from src.infra.entities import Species as SpeciesModel
from src.infra.config import DBConnectionHandler
from src.infra.test import reset_auto_increment
from .specie_repository import SpecieRepository


faker = Faker("pt_BR")
specie_repository = SpecieRepository()
db_connection = DBConnectionHandler()


@pytest.mark.skip(reason="Sensive test")
def test_insert_specie():
    """
    Should insert specie in specie table and return it
    """
    specie_name = faker.name()

    new_specie = specie_repository.insert_specie(specie_name)
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        query_specie = connection.execute(
            text("SELECT * FROM species WHERE id=:id"), {"id": new_specie.id}
        ).fetchone()

        connection.execute(
            text("DELETE FROM species WHERE id=:id"), {"id": new_specie.id}
        )
        connection.commit()

    assert new_specie.id == query_specie.id
    assert new_specie.specie_name == query_specie.specie_name

    reset_auto_increment("pets")



@pytest.mark.skip(reason="Sensive test")
def test_select_specie():
    """
    Should select specie in species table and return it
    """

    id = faker.random_number(digits=5)
    specie_name = faker.name()

    data = SpeciesModel(id=id, specie_name=specie_name)

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text("INSERT INTO species (id, specie_name) VALUES (:id, :specie_name)"),
            {
                "id": id,
                "specie_name": specie_name,
            },
        )
        connection.commit()

        query_specie1 = specie_repository.select_specie(id=data.id)
        query_specie2 = specie_repository.select_specie(specie_name=data.specie_name)
        query_specie3 = specie_repository.select_specie(
            id=data.id, specie_name=data.specie_name
        )

        connection.execute(text("DELETE FROM species WHERE id=:id"), {"id": data.id})
        connection.commit()

    assert data in query_specie1
    assert data in query_specie2
    assert data in query_specie3

    reset_auto_increment("pets")



@pytest.mark.skip(reason="Sensive test")
def test_delete_specie():
    """
    Should delete specie in species table and return bool
    """
    id = faker.random_number(digits=5)
    specie_name = faker.name()

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO species (id, specie_name) \
                    VALUES (:id, :specie_name)"
            ),
            {
                "id": id,
                "specie_name": specie_name,
            },
        )
        connection.commit()

    deleted_element = specie_repository.delete_specie(id=id)

    assert deleted_element is True

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM species WHERE id = :id"), {"id": id}
        ).fetchone()
        assert result is None

    reset_auto_increment("pets")



@pytest.mark.skip(reason="Sensive test")
def test_update_specie():
    """
    Should update specie data in the species table and return the updated object
    """
    id = faker.random_number(digits=5)
    specie_name = "Fake Specie One"
    new_specie_name = "Fake Specie Two"

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO species (id, specie_name) \
                    VALUES (:id, :specie_name)"
            ),
            {
                "id": id,
                "specie_name": specie_name,
            },
        )
        connection.commit()

    updated_specie = specie_repository.update_specie(
        id=id, new_specie_name=new_specie_name
    )

    assert updated_specie is not None
    assert updated_specie.specie_name == new_specie_name
    assert updated_specie.id == id

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT specie_name FROM species WHERE id = :id"), {"id": id}
        ).fetchone()

        connection.execute(text("DELETE FROM species WHERE id=:id"), {"id": id})
        connection.commit()

    assert result is not None
    assert result[0] == new_specie_name

    reset_auto_increment("pets")
