import logging
import datetime
from typing import List
from sqlalchemy.exc import NoResultFound
from src.data.interfaces import AddressRepositoryInterface
from src.domain.models import Addresses
from src.infra.config import DBConnectionHandler
from src.infra.entities import Addresses as AddressesModel


class AddressRepository(AddressRepositoryInterface):
    """
    Class to manage Address Repository
    """

    def __init__(self):

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )

    def insert_address(
        self,
        cep: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
        complement: str = None,
    ) -> Addresses:
        """
        Insert data in address entity
        :param  - cep: cep of the address owner
                - state: state of the address owner
                - city: city of the address owner
                - neighborhood: id of address owner
                - street: id of address owner
                - number: id of address owner
                - complement: id of address owner if it exists
        :return - tuble with new address inserted
        """
        created_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                new_address = AddressesModel(
                    cep=cep,
                    state=state,
                    city=city,
                    neighborhood=neighborhood,
                    street=street,
                    number=number,
                    complement=complement,
                    created_at=created_at,
                    updated_at=created_at,
                    deleted_at=None,
                )
                db_connection.session.add(new_address)
                self.log.info("New address added to session, committing to database.")

                db_connection.session.commit()
                self.log.info("New address committed to database successfully.")

                return Addresses(
                    id=new_address.id,
                    cep=new_address.cep,
                    state=new_address.state,
                    city=new_address.city,
                    neighborhood=new_address.neighborhood,
                    street=new_address.street,
                    number=new_address.number,
                    complement=new_address.complement,
                )

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error("Error occurred while inserting new address, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after inserting address.")
        return None



    def select_address(
        self,
        address_id: int = None,
        cep: str = None,
        state: str = None,
        city: str = None,
        neighborhood: str = None,
        street: str = None,
        number: str = None,
    ) -> List[Addresses]:
        """
        Select data into address entity
        :param  - id: id of address
                - state: state of the address
                - city: city of the address
                - neighborhood: neighborhood of the address
                - street: street of the address
                - number: number of the address
        :return - turple with selected addresses
        """

        try:
            data_query = None

            if address_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(AddressesModel).filter_by(id=address_id).one()
                    self.log.info(f"Address with id {address_id} selected from database.")
                    data_query = [data]

            elif cep and state and city and neighborhood and street and number:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AddressesModel)
                        .filter_by(
                            cep=cep,
                            state=state,
                            city=city,
                            neighborhood=neighborhood,
                            street=street,
                            number=number,
                        )
                        .filter_by(deleted_at=None)
                        .one()
                    )
                    self.log.info("Address with specified details selected from database.")

                    data_query = [data]

            elif cep or state or city or neighborhood:
                with DBConnectionHandler() as db_connection:

                    filters = {}
                    if cep:
                        filters["cep"] = cep
                        self.log.info(f"Filtering addresses by cep: {cep}")
                    if state:
                        filters["state"] = state
                        self.log.info(f"Filtering addresses by state: {state}")
                    if city:
                        filters["city"] = city
                        self.log.info(f"Filtering addresses by city: {city}")
                    if neighborhood:
                        filters["neighborhood"] = neighborhood
                        self.log.info(f"Filtering addresses by neighborhood: {neighborhood}")

                    query = db_connection.session.query(AddressesModel).filter_by(**filters).filter_by(deleted_at=None)
                    data_query = query.all()
                    self.log.info("Addresses selected from database based on provided filters.")

            return data_query

        except NoResultFound:
            return []

        except:
            with DBConnectionHandler() as db_connection:
                db_connection.session.rollback()
                self.log.error("Error occurred while selecting address, rolling back transaction.")
            raise

        finally:
            with DBConnectionHandler() as db_connection:
                db_connection.session.close()
                self.log.info("Database session closed after selecting address.")



    def delete_address(self, id: int) -> bool:
        """
        Delete data from address entity
        :param  - id: id of the address to be deleted
        :return - True if the address was deleted, False otherwise
        """
        deleted_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                address_to_delete = db_connection.session.query(AddressesModel).filter_by(id=id).filter_by(deleted_at=None).one_or_none()
                self.log.info(f"Attempting to delete address with id {id}.")

                if address_to_delete:
                    address_to_delete.deleted_at = deleted_at
                    address_to_delete.updated_at = deleted_at
                    db_connection.session.commit()
                    self.log.info(f"Address with id {id} deleted successfully.")
                    return True

                self.log.info(f"Address with id {id} not found or already deleted.")
                return False

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while deleting address with id {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after deleting address.")



    def update_address(self, id: int, **kwargs: any) -> Addresses:
        """
        Update data in address entity
        :param  - id: id of the address to be updated
                - **kwargs: dictionary containing fields and their new values
        :return - Updated address data as an instance of UserAdopters, or None if not found
        """

        updated_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                address_to_update = db_connection.session.query(AddressesModel).filter_by(id=id).filter_by(deleted_at=None).one_or_none()
                self.log.info(f"Attempting to update address with id {id}.")

                if address_to_update:
                    # Update params based into kwargs
                    for key, value in kwargs.items():
                        if hasattr(address_to_update, key):
                            setattr(address_to_update, key, value)
                            self.log.info(f"Updated {key} of address id {id} to {value}.")

                    address_to_update.updated_at = updated_at

                    db_connection.session.commit()
                    self.log.info(f"Address with id {id} updated successfully.")

                    return Addresses(
                        id=address_to_update.id,
                        cep=address_to_update.cep,
                        state=address_to_update.state,
                        city=address_to_update.city,
                        neighborhood=address_to_update.neighborhood,
                        street=address_to_update.street,
                        number=address_to_update.number,
                        complement=address_to_update.complement,
                    )
                return None

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while updating address with id {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after updating address.")
