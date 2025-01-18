from sqlalchemy import text
from faker import Faker
from src.infra.entities import UserAdopters as UserAdoptersModel
from src.infra.config import DBConnectionHandler
from .user_adopter_repository import UserAdopterRepository


faker = Faker("pt_BR")
user_adopter_repository = UserAdopterRepository()
db_connection = DBConnectionHandler()


def test_insert_user_adopter():
    """
    Should insert user_adopter in user_adopter table and return it
    """
    name = faker.name()
    cpf = faker.cpf().replace(".", "").replace("-", "")
    email = faker.email()
    phone_number = str(faker.random_number(digits=11))
    address_id = faker.random_number(digits=2)
    pet_id = faker.random_number(digits=2)

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


def test_select_user_adopter():
    """
    Should select user_adopters in user_adopter table and return it
    """

    user_adopter_id = faker.random_number(digits=5)
    name = faker.name()
    cpf = faker.cpf().replace(".", "").replace("-", "")
    email = faker.email()
    phone_number = str(faker.random_number(digits=11)).zfill(11)
    address_id = faker.random_number(digits=2)
    pet_id = faker.random_number(digits=2)

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
        query_user_adopter5 = user_adopter_repository.select_user_adopter(
            pet_id=data.pet_id
        )

        connection.execute(
            text("DELETE FROM user_adopters WHERE id=:id"), {"id": data.id}
        )
        connection.commit()

    assert data in query_user_adopter1
    assert data in query_user_adopter2
    assert data in query_user_adopter3
    assert data in query_user_adopter4
    assert data in query_user_adopter5
