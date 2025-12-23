import logging
import pytest
from sqlalchemy import text
from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import AnimalShelters as AnimalSheltersModel
from src.infra.test import reset_auto_increment
from .animal_shelter_repository import AnimalShelterRepository


faker = Faker("pt_BR")
animal_shelter_repository = AnimalShelterRepository()
db_connection = DBConnectionHandler()


# @pytest.mark.skip(reason="Sensive test. Repository interaction test")
def test_insert_animal_shelter():
    """
    Should insert animal_shelter
    """

    # generate random values for testing
    name = faker.name()
    password = faker.password(
        length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
    )
    cpf = faker.cpf().replace(".", "").replace("-", "")
    responsible_name = faker.name()
    email = faker.email()
    phone_number = str(faker.random_number(digits=11))
    address_id = faker.random_number(digits=5)

    # address params
    cep = str(faker.random_number(digits=8))
    state = faker.state_abbr()
    city = faker.city()
    neighborhood = faker.name()
    street = faker.name()
    number = faker.random_number(digits=2)

    # connection with database
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        # insert the random values into the database using SQL commands
        connection.execute(
            text(
                "INSERT INTO addresses (id, cep, state, city, neighborhood, street, number) \
                    VALUES (:id, :cep, :state, :city, :neighborhood, :street, :number)"
            ),
            {
                "id": address_id,
                "cep": cep,
                "state": state,
                "city": city,
                "neighborhood": neighborhood,
                "street": street,
                "number": number,
            },
        )
        connection.commit()

    # insert the generated random values into database
    new_animal_shelter = animal_shelter_repository.insert_animal_shelter(
        name, password, cpf, responsible_name, email, phone_number, address_id
    )

    with engine.connect() as connection:
        # retrieve the inserted values from the database using SQL
        query_animal_shelter = connection.execute(
            text("SELECT * FROM animal_shelters WHERE id=:id"),
            {"id": new_animal_shelter.id},
        ).fetchone()

        # remove the test data from the database
        connection.execute(
            text("DELETE FROM animal_shelters WHERE id=:id"),
            {"id": new_animal_shelter.id},
        )
        connection.commit()

        # clean up the database after the tests
        connection.execute(
            text("DELETE FROM addresses WHERE id=:id"), {"id": address_id}
        )
        connection.commit()

    # compare the inserted value with the retrieved values from db
    assert new_animal_shelter.id == query_animal_shelter.id
    assert new_animal_shelter.name == query_animal_shelter.name
    assert new_animal_shelter.password == query_animal_shelter.password
    assert new_animal_shelter.cpf == query_animal_shelter.cpf
    assert new_animal_shelter.responsible_name == query_animal_shelter.responsible_name
    assert new_animal_shelter.email == query_animal_shelter.email
    assert new_animal_shelter.phone_number == query_animal_shelter.phone_number
    assert new_animal_shelter.address_id == query_animal_shelter.address_id

    reset_auto_increment("addresses")
    reset_auto_increment("animal_shelters")



# @pytest.mark.skip(reason="Sensive test. Repository interaction test")
def test_select_animal_shelter():
    """
    Shoul select a animal_shelter in AnimalShelters table and compare it with
    """

    # generet random values for testing
    id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.password(
        length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
    )
    cpf = faker.cpf().replace(".", "").replace("-", "")
    responsible_name = faker.name()
    email = faker.email()
    phone_number = str(faker.random_number(digits=11)).zfill(11)
    address_id = faker.random_number(digits=5)

    # address params
    cep = str(faker.random_number(digits=8))
    state = faker.state_abbr()
    city = faker.city()
    neighborhood = faker.name()
    street = faker.name()
    number = faker.random_number(digits=2)

    # connection with database
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        # insert the random values into the database using SQL commands
        connection.execute(
            text(
                "INSERT INTO addresses (id, cep, state, city, neighborhood, street, number) \
                    VALUES (:id, :cep, :state, :city, :neighborhood, :street, :number)"
            ),
            {
                "id": address_id,
                "cep": cep,
                "state": state,
                "city": city,
                "neighborhood": neighborhood,
                "street": street,
                "number": number,
            },
        )
        connection.commit()

    # save the random values into a 'data' variable for comparison
    data = AnimalSheltersModel(
        id=id,
        name=name,
        password=password,
        cpf=cpf,
        responsible_name=responsible_name,
        email=email,
        phone_number=phone_number,
        address_id=address_id,
    )

    with engine.connect() as connection:
        # insert the random values into the database using SQL commands
        connection.execute(
            text(
                "INSERT INTO animal_shelters (id, name, password, cpf, responsible_name, email, phone_number, address_id) \
                    VALUES (:id, :name, :password, :cpf, :responsible_name, :email, :phone_number, :address_id)"
            ),
            {
                "id": id,
                "name": name,
                "password": password,
                "cpf": cpf,
                "responsible_name": responsible_name,
                "email": email,
                "phone_number": phone_number,
                "address_id": address_id,
            },
        )
        connection.commit()

        # run tests on the select_animal_shelter function to verify all use cases and saving in memory
        query_animal_shelter1 = animal_shelter_repository.select_animal_shelter(
            id=data.id
        )
        query_animal_shelter2 = animal_shelter_repository.select_animal_shelter(
            name=data.name
        )
        query_animal_shelter3 = animal_shelter_repository.select_animal_shelter(
            id=data.id, name=data.name
        )
        query_animal_shelter4 = animal_shelter_repository.select_animal_shelter(
            cpf=data.cpf
        )
        query_animal_shelter5 = animal_shelter_repository.select_animal_shelter(
            address_id=data.address_id
        )

        # clean up the database after the tests
        connection.execute(
            text("DELETE FROM animal_shelters WHERE id=:id"), {"id": data.id}
        )
        connection.commit()

        # clean up the database after the tests
        connection.execute(
            text("DELETE FROM addresses WHERE id=:id"), {"id": data.address_id}
        )
        connection.commit()

    # compare the random values with the data retrieved from the database
    assert data in query_animal_shelter1
    assert data in query_animal_shelter2
    assert data in query_animal_shelter3
    assert data in query_animal_shelter4
    assert data in query_animal_shelter5

    reset_auto_increment("addresses")
    reset_auto_increment("animal_shelters")



# @pytest.mark.skip(reason="Sensive test. Repository interaction test")
def test_delete_animal_shelter():
    """
    Should delete animal_shelter in animal_shelters table and return bool
    """
    id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.password(
        length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
    )
    cpf = faker.cpf().replace(".", "").replace("-", "")
    responsible_name = faker.name()
    email = faker.email()
    phone_number = str(faker.random_number(digits=11)).zfill(11)
    address_id = None

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO animal_shelters (id, name, password, cpf, responsible_name, email, phone_number, address_id) \
                    VALUES (:id, :name, :password, :cpf, :responsible_name, :email, :phone_number, :address_id)"
            ),
            {
                "id": id,
                "name": name,
                "password": password,
                "cpf": cpf,
                "responsible_name": responsible_name,
                "email": email,
                "phone_number": phone_number,
                "address_id": address_id,
            },
        )
        connection.commit()

    deleted_element = animal_shelter_repository.delete_animal_shelter(id=id)

    assert deleted_element is True

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM animal_shelters WHERE id = :id"), {"id": id}
        ).fetchone()
        assert result is None

    reset_auto_increment("addresses")
    reset_auto_increment("animal_shelters")



# @pytest.mark.skip(reason="Sensive test. Repository interaction test")
def test_update_animal_shelter():
    """
    Should update animal_shelter data in the sanimal_shelters table and return the updated object
    """
    id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.password(
        length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
    )
    cpf = faker.cpf().replace(".", "").replace("-", "")
    responsible_name = faker.name()
    email = faker.email()
    phone_number = str(faker.random_number(digits=11)).zfill(11)
    address_id = None

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO animal_shelters (id, name, password, cpf, responsible_name, email, phone_number, address_id) \
                    VALUES (:id, :name, :password, :cpf, :responsible_name, :email, :phone_number, :address_id)"
            ),
            {
                "id": id,
                "name": name,
                "password": password,
                "cpf": cpf,
                "responsible_name": responsible_name,
                "email": email,
                "phone_number": phone_number,
                "address_id": address_id,
            },
        )
        connection.commit()

    new_name = faker.name()
    new_email = faker.email()
    update_data = {
        "name": new_name,
        "email": new_email,
    }

    updated_animal_shelter = animal_shelter_repository.update_animal_shelter(id=id, **update_data)

    assert updated_animal_shelter is not None
    assert updated_animal_shelter.name == new_name
    assert updated_animal_shelter.email == new_email
    assert updated_animal_shelter.id == id

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT name, email FROM animal_shelters WHERE id = :id"), {"id": id}
        ).fetchone()

        connection.execute(text("DELETE FROM animal_shelters WHERE id=:id"), {"id": id})
        connection.commit()

    assert result is not None
    assert result[0] == new_name
    assert result[1] == new_email

    reset_auto_increment("addresses")
    reset_auto_increment("animal_shelters")
