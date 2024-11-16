from sqlalchemy import text
from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from .user_repository import UserRepository


faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """
    Should insert user
    """

    # generate random values for testing
    name = faker.name()
    password = faker.password()

    # connect to the database
    engine = db_connection_handler.get_engine()

    # insert the generated random values into database
    new_user = user_repository.insert_user(name, password)

    with engine.connect() as connection:
        # retrieve the inserted values from the database using SQL
        query_user = connection.execute(
            text("SELECT * FROM users WHERE id=:id"), {"id": new_user.id}
        ).fetchone()

        # remove the test data from the database
        connection.execute(text("DELETE FROM users WHERE id=:id"), {"id": new_user.id})
        connection.commit()

    # compare the inserted value with the retrieved values from db
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """
    Shoul select a user in Users table and compare it with
    """

    # generet random values for testing
    user_id = faker.random_number(digits=5)
    user_name = faker.name()
    user_password = faker.password()

    # save the random values into a 'data' variable for comparison
    data = UsersModel(id=user_id, name=user_name, password=user_password)

    engine = db_connection_handler.get_engine()

    with engine.connect() as connection:
        # insert the random values into the database using SQL commands
        connection.execute(
            text(
                "INSERT INTO users (id, name, password) VALUES (:id, :name, :password)"
            ),
            {"id": user_id, "name": user_name, "password": user_password},
        )
        connection.commit()

        # run tests on the select_user function to verify all use cases and saving in memory
        query_user1 = user_repository.select_user(user_id=data.id)
        query_user2 = user_repository.select_user(name=data.name)
        query_user3 = user_repository.select_user(user_id=data.id, name=data.name)

        # clean up the database after the tests
        connection.execute(text("DELETE FROM users WHERE id=:id"), {"id": data.id})
        connection.commit()

    # compare the random values with the data retrieved from the database
    assert data in query_user1
    assert data in query_user2
    assert data in query_user3
