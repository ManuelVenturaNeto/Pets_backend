# pylint: disable=R0914

from sqlalchemy import text
from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import AnimalShelters as AnimalSheltersModel
from .animal_shelter_repository import AnimalShelterRepository


faker = Faker("pt_BR")
animal_shelter_repository = AnimalShelterRepository()
db_connection = DBConnectionHandler()


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
