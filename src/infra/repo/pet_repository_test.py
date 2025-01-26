import pytest
from sqlalchemy import text
from faker import Faker
from src.infra.entities import Pets as PetsModel
from src.infra.config import DBConnectionHandler
from src.infra.test import reset_auto_increment
from .pet_repository import PetRepository


faker = Faker("pt_BR")
pet_repository = PetRepository()
db_connection = DBConnectionHandler()


@pytest.mark.skip(reason="Sensive test")
def test_insert_pet():
    """
    Should insert pet in pet table and return it
    """
    name = faker.name()
    specie = faker.random_int(min=1, max=10)
    age = faker.random_number(digits=2)
    animal_shelter_id = None
    adopted = False

    new_pet = pet_repository.insert_pet(name, specie, age, animal_shelter_id, adopted)
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        query_pet = connection.execute(
            text("SELECT * FROM pets WHERE id=:id"), {"id": new_pet.id}
        ).fetchone()

        connection.execute(text("DELETE FROM pets WHERE id=:id"), {"id": new_pet.id})
        connection.commit()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.animal_shelter_id == query_pet.animal_shelter_id
    assert new_pet.adopted == query_pet.adopted

    reset_auto_increment("pets")


@pytest.mark.skip(reason="Sensive test")
def test_select_pet():
    """
    Should select pets in pet table and return it
    """

    pet_id = faker.random_number(digits=5)
    name = faker.name()
    specie = faker.random_int(min=1, max=10)
    age = faker.random_number(digits=2)
    animal_shelter_id = None
    adopted = False

    data = PetsModel(
        id=pet_id,
        name=name,
        specie=specie,
        age=age,
        animal_shelter_id=animal_shelter_id,
        adopted=adopted,
    )

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO pets (id, name, specie, age, animal_shelter_id, adopted) \
                    VALUES (:id, :name, :specie, :age, :animal_shelter_id, :adopted)"
            ),
            {
                "id": pet_id,
                "name": name,
                "specie": specie,
                "age": age,
                "animal_shelter_id": animal_shelter_id,
                "adopted": adopted,
            },
        )
        connection.commit()

        query_pet1 = pet_repository.select_pet(pet_id=data.id)
        # query_pet2 = pet_repository.select_pet(animal_shelter_id=data.animal_shelter_id)
        query_pet3 = pet_repository.select_pet(
            pet_id=data.id, animal_shelter_id=data.animal_shelter_id
        )

        connection.execute(text("DELETE FROM pets WHERE id=:id"), {"id": data.id})
        connection.commit()

    assert data in query_pet1
    # assert data in query_pet2
    assert data in query_pet3

    reset_auto_increment("pets")


@pytest.mark.skip(reason="Sensive test")
def test_delete_pet():
    """
    Should delete pet in pet table and return bool
    """
    id = faker.random_number(digits=5)
    name = faker.name()
    specie = faker.random_int(min=1, max=10)
    age = faker.random_number(digits=2)
    animal_shelter_id = None
    adopted = False

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO pets (id, name, specie, age, animal_shelter_id, adopted) \
                    VALUES (:id, :name, :specie, :age, :animal_shelter_id, :adopted)"
            ),
            {
                "id": id,
                "name": name,
                "specie": specie,
                "age": age,
                "animal_shelter_id": animal_shelter_id,
                "adopted": adopted,
            },
        )
        connection.commit()

    deleted_element = pet_repository.delete_pet(id=id)

    assert deleted_element is True

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM pets WHERE id = :id"), {"id": id}
        ).fetchone()
        assert result is None

    reset_auto_increment("pets")


@pytest.mark.skip(reason="Sensive test")
def test_update_pets():
    """
    Should update pet data in the pets table and return the updated object
    """
    id = faker.random_number(digits=5)
    name = faker.name()
    specie = faker.random_int(min=1, max=10)
    age = faker.random_number(digits=2)
    animal_shelter_id = None
    adopted = False

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO pets (id, name, specie, age, animal_shelter_id, adopted) \
                    VALUES (:id, :name, :specie, :age, :animal_shelter_id, :adopted)"
            ),
            {
                "id": id,
                "name": name,
                "specie": specie,
                "age": age,
                "animal_shelter_id": animal_shelter_id,
                "adopted": adopted,
            },
        )
        connection.commit()

    # Dados para atualização
    new_name = faker.name()
    status_adopted = True
    update_data = {
        "name": new_name,
        "adopted": status_adopted,
    }

    updated_pet = pet_repository.update_pet(id=id, **update_data)

    assert updated_pet is not None
    assert updated_pet.name == new_name
    assert updated_pet.adopted == status_adopted
    assert updated_pet.id == id

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT name, adopted FROM pets WHERE id = :id"), {"id": id}
        ).fetchone()

        connection.execute(text("DELETE FROM pets WHERE id=:id"), {"id": id})
        connection.commit()

    assert result is not None
    assert result[0] == new_name
    assert result[1] == status_adopted

    reset_auto_increment("pets")
