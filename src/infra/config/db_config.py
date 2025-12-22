import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db_base import Base


from dotenv import load_dotenv
load_dotenv()

class DBConnectionHandler:
    """
    Class to manage database connections using SQLAlchemy.
    """
    def __init__(self):
        db_host = str(os.getenv("DB_HOST"))
        db_port = str(os.getenv("DB_PORT"))
        db_user = str(os.getenv("DB_USER"))
        db_password = str(os.getenv("DB_PASSWORD"))
        db_name = str(os.getenv("DB_NAME"))

        self.__connection_string = (
            f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
        self.__engine = self.__create_database_engine()
        self.session = None



    def __create_database_engine(self):
        """
        Create and return a SQLAlchemy engine.
        """
        engine = create_engine(self.__connection_string)
        return engine



    def get_engine(self):
        """
        Return the SQLAlchemy engine instance.
        """
        return self.__engine



    def __enter__(self):
        """
        Open a database session.
        """
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self



    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the database session.
        """
        self.session.close()



    def create_tables(self):
        """
        Create all tables in the database.
        """
        Base.metadata.create_all(bind=self.__engine)