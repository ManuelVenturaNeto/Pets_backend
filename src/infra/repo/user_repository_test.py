from sqlalchemy import text
from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository


faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """
    Should insert user
    """

    name = faker.name()
    password = faker.password()
    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_user = user_repository.insert_user(name, password)

    # Utilizando o método connect() corretamente
    with engine.connect() as connection:
        query_user = connection.execute(
            text("SELECT * FROM users WHERE id=:id"), {"id": new_user.id}
        ).fetchone()

        connection.execute(text("DELETE FROM users WHERE id=:id"), {"id": new_user.id})
        connection.commit()

    # Asserções
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
