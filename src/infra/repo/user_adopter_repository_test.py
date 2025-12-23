import pytest
from sqlalchemy import text
from faker import Faker
from src.infra.entities import UserAdopters as UserAdoptersModel
from src.infra.config import DBConnectionHandler
from src.infra.test import reset_auto_increment
from .user_adopter_repository import UserAdopterRepository


faker = Faker("pt_BR")
user_adopter_repository = UserAdopterRepository()
db_connection = DBConnectionHandler()


@pytest.mark.skip(reason="Sensive test. Repository interaction test")
def test_insert_user_adopter():
    """
    Should insert user_adopter in user_adopter table and return it
    """
    name = faker.name()
    cpf = faker.cpf().replace(".", "").replace("-", "")
    email = faker.email()
    phone_number = str(faker.random_number(digits=11))
    address_id = None
    pet_id = None

    new_user_adopter = user_adopter_repository.insert_user_adopter(
        name, cpf, email, phone_number, address_id, pet_id
    )
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        query_user_adopter = connection.execute(
            text("SELECT * FROM user_adopters WHERE id=:id"),
            {"id": new_user_adopter.id},
        ).fetchone()

        connection.execute(
            text("DELETE FROM user_adopters WHERE id=:id"), {"id": new_user_adopter.id}
        )
        connection.commit()

    assert new_user_adopter.id == query_user_adopter.id
    assert new_user_adopter.name == query_user_adopter.name
    assert new_user_adopter.cpf == query_user_adopter.cpf
    assert new_user_adopter.email == query_user_adopter.email
    assert new_user_adopter.phone_number == query_user_adopter.phone_number
    assert new_user_adopter.address_id == query_user_adopter.address_id
    assert new_user_adopter.pet_id == query_user_adopter.pet_id

    reset_auto_increment("user_adopters")



@pytest.mark.skip(reason="Sensive test. Repository interaction test")
def test_select_user_adopter():
    """
    Should select user_adopters in user_adopter table and return it
    """

    user_adopter_id = faker.random_number(digits=5)
    name = faker.name()
    cpf = faker.cpf().replace(".", "").replace("-", "")
    email = faker.email()
    phone_number = str(faker.random_number(digits=11)).zfill(11)
    address_id = None
    pet_id = None

    data = UserAdoptersModel(
        id=user_adopter_id,
        name=name,
        cpf=cpf,
        email=email,
        phone_number=phone_number,
        address_id=address_id,
        pet_id=pet_id,
    )

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO user_adopters (id, name, cpf, email, phone_number, address_id, pet_id) \
                    VALUES (:id, :name, :cpf, :email, :phone_number, :address_id, :pet_id)"
            ),
            {
                "id": user_adopter_id,
                "name": name,
                "cpf": cpf,
                "email": email,
                "phone_number": phone_number,
                "address_id": address_id,
                "pet_id": pet_id,
            },
        )
        connection.commit()

        query_user_adopter1 = user_adopter_repository.select_user_adopter(id=data.id)
        query_user_adopter2 = user_adopter_repository.select_user_adopter(
            id=data.id, cpf=data.phone_number
        )
        query_user_adopter3 = user_adopter_repository.select_user_adopter(cpf=data.cpf)
        query_user_adopter4 = user_adopter_repository.select_user_adopter(
            cpf=data.cpf,
            email=data.email,
            phone_number=data.phone_number,
            address_id=data.address_id,
            pet_id=data.pet_id,
        )
        # query_user_adopter5 = user_adopter_repository.select_user_adopter(
        #     pet_id=data.pet_id
        # )

        connection.execute(
            text("DELETE FROM user_adopters WHERE id=:id"), {"id": data.id}
        )
        connection.commit()

    assert data in query_user_adopter1
    assert data in query_user_adopter2
    assert data in query_user_adopter3
    assert data in query_user_adopter4
    # assert data in query_user_adopter5

    reset_auto_increment("user_adopters")



@pytest.mark.skip(reason="Sensive test. Repository interaction test")
def test_delete_user_adopter():
    """
    Should delete user_adopter in user_adopter table and return bool
    """
    id = faker.random_number(digits=5)
    name = faker.name()
    cpf = faker.cpf().replace(".", "").replace("-", "")
    email = faker.email()
    phone_number = str(faker.random_number(digits=11))
    address_id = None
    pet_id = None

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO user_adopters (id, name, cpf, email, phone_number, address_id, pet_id) \
                    VALUES (:id, :name, :cpf, :email, :phone_number, :address_id, :pet_id)"
            ),
            {
                "id": id,
                "name": name,
                "cpf": cpf,
                "email": email,
                "phone_number": phone_number,
                "address_id": address_id,
                "pet_id": pet_id,
            },
        )
        connection.commit()

    deleted_element = user_adopter_repository.delete_user_adopter(id=id)

    assert deleted_element is True

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM user_adopters WHERE id = :id"), {"id": id}
        ).fetchone()
        assert result is None

    reset_auto_increment("user_adopters")



@pytest.mark.skip(reason="Sensive test. Repository interaction test")
def test_update_user_adopter():
    """
    Should update user_adopter data in the user_adopters table and return the updated object
    """
    id = faker.random_number(digits=5)
    name = faker.name()
    cpf = faker.cpf().replace(".", "").replace("-", "")
    email = faker.email()
    phone_number = str(faker.random_number(digits=11))
    address_id = None
    pet_id = None

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO user_adopters (id, name, cpf, email, phone_number, address_id, pet_id) \
                    VALUES (:id, :name, :cpf, :email, :phone_number, :address_id, :pet_id)"
            ),
            {
                "id": id,
                "name": name,
                "cpf": cpf,
                "email": email,
                "phone_number": phone_number,
                "address_id": address_id,
                "pet_id": pet_id,
            },
        )
        connection.commit()

    new_name = faker.name()
    new_email = faker.email()
    update_data = {
        "name": new_name,
        "email": new_email,
    }

    updated_user_adopter = user_adopter_repository.update_user_adopter(
        id=id, **update_data
    )

    assert updated_user_adopter is not None
    assert updated_user_adopter.name == new_name
    assert updated_user_adopter.email == new_email
    assert updated_user_adopter.id == id

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT name, email FROM user_adopters WHERE id = :id"), {"id": id}
        ).fetchone()

        connection.execute(text("DELETE FROM user_adopters WHERE id=:id"), {"id": id})
        connection.commit()

    assert result is not None
    assert result[0] == new_name
    assert result[1] == new_email

    reset_auto_increment("user_adopters")
