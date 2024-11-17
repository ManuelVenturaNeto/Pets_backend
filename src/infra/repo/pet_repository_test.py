from sqlalchemy import text
from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities.pets import AnimalTypes
from .pet_repository import PetRepository


faker = Faker()
pet_repository = PetRepository()
db_connection = DBConnectionHandler()


def test_insert_pet():
    """
    Should insert pet in pet table and return it
    """
    name = faker.name()
    species = faker.enum(AnimalTypes)
    age = faker.random_number()
    user_id = faker.random_number()

    new_pet = pet_repository.insert_pet(name, species, age, user_id)
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        query_pet = connection.execute(
            text("SELECT * FROM pets WHERE id=:id"), {"id": new_pet.id}
        ).fetchone()

        connection.execute(text("DELETE FROM pets WHERE id=:id"), {"id": new_pet.id})
        connection.commit()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.species == query_pet.species
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id
