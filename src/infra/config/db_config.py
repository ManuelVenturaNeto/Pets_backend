"""
This file is responsible for creating a connection to the database using an ORM (SQLAlchemy).
"""

# import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from sqlalchemy.engine.url import URL


class DBConnectionHandler:
    """
    Class to manage database connections using SQLAlchemy.
    """

    # ========== SQLITE ==========

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

    # ========== MYSQL ==========

    # def __init__(self):
    #     self.__connection_string = URL.create(
    #         drivername='mysql+pymysql',
    #         username='root',
    #         password=os.getenv("MYSQLPASSWORD"),
    #         host='172.17.0.2',
    #         port=3306,
    #         database='pets_backend_db'
    #     )
    #     self.__engine = self.__create_database_engine()
    #     self.session = None

    # def __create_database_engine(self):
    #     engine = create_engine(self.__connection_string)
    #     return engine

    # def get_engine(self):
    #     return self.__engine

    # def __enter__(self):
    #     session_make = sessionmaker(bind=self.__engine)
    #     self.session = session_make()
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.session.close()
