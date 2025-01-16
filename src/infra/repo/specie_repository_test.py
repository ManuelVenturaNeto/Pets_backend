from sqlalchemy import text
from faker import Faker
from src.infra.entities import Species as SpeciesModel
from src.infra.config import DBConnectionHandler
from .specie_repository import SpecieRepository


faker = Faker("pt_BR")
specie_repository = SpecieRepository()
db_connection = DBConnectionHandler()


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


def test_select_specie():
    """
    Should select species in specie table and return it
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
