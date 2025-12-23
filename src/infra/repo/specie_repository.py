import logging
import datetime
from typing import List
from sqlalchemy.exc import NoResultFound
from src.data.interfaces import SpecieRepositoryInterface
from src.domain.models import Species
from src.infra.config import DBConnectionHandler
from src.infra.entities import Species as SpeciesModel


class SpecieRepository(SpecieRepositoryInterface):
    """
    Class to manage Specie Repository
    """

    def __init__(self):

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )

    def insert_specie(self, specie_name: str) -> Species:
        """
        Insert data in specie entity
        :param  - name: name of specie
        :return - tuble with new specie inserted
        """
        created_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                new_specie = SpeciesModel(
                    specie_name=specie_name,
                    created_at=created_at,
                    updated_at=created_at,
                    deleted_at=None
                )
                db_connection.session.add(new_specie)
                self.log.info(f"Inserting new specie: {specie_name}")

                db_connection.session.commit()
                self.log.info(f"New specie inserted with ID: {new_specie.id}")

                return Species(
                    id=new_specie.id,
                    specie_name=new_specie.specie_name,
                )

            except:
                db_connection.session.rollback()
                self.log.error(f"Error occurred while inserting specie {specie_name}, rolling back transaction.")
                raise

            finally:
                db_connection.session.close()
                self.log.info("Database session closed after inserting specie.")
        return None



    def select_specie(self, id: int = None, specie_name: int = None) -> List[Species]:
        """
        Select data into specie entity
        :param  - id: id of specie
                - specie_name: id of owner
        :return - turple with selected specie
        """

        try:
            data_query = None

            if id and not specie_name:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(SpeciesModel).filter_by(id=id).filter_by(deleted_at=None).one()
                    data_query = [data]
                    self.log.info(f"Specie with ID {id} selected successfully.")

            elif not id and specie_name:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(SpeciesModel).filter_by(specie_name=specie_name).filter_by(deleted_at=None).one()
                    data_query = [data]
                    self.log.info(f"Specie with name {specie_name} selected successfully.")

            elif id and specie_name:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(SpeciesModel).filter_by(id=id, specie_name=specie_name).filter_by(deleted_at=None).one()
                    data_query = [data]
                    self.log.info(f"Specie with ID {id} and name {specie_name} selected successfully.")

            return data_query

        except NoResultFound:
            self.log.warning(f"No specie found for ID {id} and name {specie_name}.")
            return []

        except:
            with DBConnectionHandler() as db_connection:
                db_connection.session.rollback()
                self.log.error("Error occurred while selecting specie, rolling back transaction.")
            raise

        finally:
            with DBConnectionHandler() as db_connection:
                db_connection.session.close()
                self.log.info("Database session closed after selecting specie.")



    def delete_specie(self, id: int) -> bool:
        """
        Delete data from specie entity
        :param  - id: id of the specie to be deleted
        :return - True if the specie was deleted, False otherwise
        """
        deleted_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                specie_to_delete = db_connection.session.query(SpeciesModel).filter_by(id=id).filter_by(deleted_at=None).one_or_none()
                self.log.info(f"Attempting to delete specie with ID {id}.")

                if specie_to_delete:
                    specie_to_delete.deleted_at = deleted_at
                    specie_to_delete.updated_at = deleted_at
                    db_connection.session.commit()
                    self.log.info(f"Specie with ID {id} deleted successfully.")
                    return True

                self.log.warning(f"Specie with ID {id} not found for deletion.")
                return False

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while deleting specie with ID {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after deleting specie.")



    def update_specie(self, id: int, new_specie_name: str) -> Species:
        """
        Update data in specie entity
        :param  - id: id of the specie to be updated
                - new_specie_name: new name for the specie
        :return - Updated specie data
        """
        updated_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                specie_to_update = db_connection.session.query(SpeciesModel).filter_by(id=id).filter_by(deleted_at=None).one_or_none()
                self.log.info(f"Attempting to update specie with ID {id}.")

                if specie_to_update:
                    specie_to_update.specie_name = new_specie_name

                    specie_to_update.updated_at = updated_at

                    db_connection.session.commit()
                    self.log.info(f"Specie with ID {id} updated successfully.")

                    return Species(
                        id=specie_to_update.id,
                        specie_name=specie_to_update.specie_name,
                    )

                self.log.warning(f"Specie with ID {id} not found for update.")
                return None

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while updating specie with ID {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after updating specie.")
