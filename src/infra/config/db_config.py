"""
This file is responsible for creating a connection to the database using an ORM (SQLAlchemy).
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """
    Class to manage database connections using SQLAlchemy.
    """

    def __init__(self):
        """
        Initializes the DBConnectionHandler with a connection string and session attributes.
        """
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """
        Return connection engine
        :param  - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
