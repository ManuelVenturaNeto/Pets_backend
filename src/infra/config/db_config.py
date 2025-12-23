import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector
from .db_base import Base

from dotenv import load_dotenv
load_dotenv()

class DBConnectionHandler:
    """
    Class to manage database connections using SQLAlchemy.
    """
    def __init__(self):
        self.db_instance = str(os.getenv("DB_INSTANCE_NAME"))
        self.db_user = str(os.getenv("DB_USER"))
        self.db_password = str(os.getenv("DB_PASSWORD"))
        self.db_name = str(os.getenv("DB_NAME"))

        self.__connector = Connector()

        self.__engine = create_engine(
            "postgresql+pg8000://",
            creator=self.get_connection
        )

        self.session = None

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )


    def get_connection(self):
        """
        Create and return a SQLAlchemy engine.
        """
        conn = self.__connector.connect(
            instance_connection_string=self.db_instance,
            driver="pg8000",
            user=self.db_user,
            password=self.db_password,
            db=self.db_name
        )
        self.log.info("Database connection established.")
        return conn



    def get_engine(self):
        """
        Return the SQLAlchemy engine instance.
        """
        self.log.info("Retrieving database engine.")
        return self.__engine



    def __enter__(self):
        """
        Open a database session.
        """
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        self.log.info("Database session opened.")
        return self



    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the database session.
        """
        self.log.info("Closing database session.")
        self.session.close()



    def create_tables(self):
        """
        Create all tables in the database.
        """
        Base.metadata.create_all(bind=self.__engine)
        self.log.info("Database tables created.")