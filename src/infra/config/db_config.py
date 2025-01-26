# pylint: disable=C0209

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """
    Class to manage database connections using SQLAlchemy.
    """

    # ========== MYSQL ==========

    def __init__(self):
        db_host = os.getenv("DB_HOST", "localhost")  # Default to 'localhost'
        db_port = os.getenv("DB_PORT", "3306")  # Default to '3306'
        db_user = os.getenv("DB_USER", "root")  # Default to 'root'
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME", "pets_backend_db")

        self.__connection_string = (
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
