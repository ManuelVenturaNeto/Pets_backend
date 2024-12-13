from sqlalchemy import text
from faker import Faker
from src.infra.entities import Pets as PetsModel
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
    species = faker.enum(AnimalTypes).name
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

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


def test_select_pet():
    """
    Should select pets in pet table and return it
    """

    pet_id = faker.random_number(digits=5)
    name = faker.name()
    species = faker.enum(AnimalTypes).name
    age = faker.random_number(digits=2)
    user_id = faker.random_number()

    data = PetsModel(id=pet_id, name=name, species=species, age=age, user_id=user_id)

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO pets (id, name, species, age, user_id) VALUES (:id, :name, :species, :age, :user_id)"
            ),
            {
                "id": pet_id,
                "name": name,
                "species": species,
                "age": age,
                "user_id": user_id,
            },
        )
        connection.commit()

        query_pet1 = pet_repository.select_pet(pet_id=data.id)
        query_pet2 = pet_repository.select_pet(user_id=data.user_id)
        query_pet3 = pet_repository.select_pet(pet_id=data.id, user_id=data.user_id)

        connection.execute(text("DELETE FROM pets WHERE id=:id"), {"id": data.id})
        connection.commit()

    assert data in query_pet1
    assert data in query_pet2
    assert data in query_pet3
