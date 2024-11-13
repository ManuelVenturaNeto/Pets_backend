from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """
    A simple Repository
    """

    @classmethod
    def insert_use(cls):
        """
        Something
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Manuel", password="Senha123")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except ImportError:
                db_connection.session.rollback()
            finally:
                db_connection.session.close()
