import logging
import datetime
from typing import List
from sqlalchemy.exc import NoResultFound
from src.data.interfaces import UserAdopterRepositoryInterface
from src.domain.models import UserAdopters
from src.infra.config import DBConnectionHandler
from src.infra.entities import UserAdopters as UserAdoptersModel


class UserAdopterRepository(UserAdopterRepositoryInterface):
    """
    Class to manemail UserAdopter Repository
    """

    def __init__(self):

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )

    def insert_user_adopter(
        self,
        name: str,
        cpf: str,
        email: str,
        phone_number: str,
        address_id: int,
        pet_id: int,
    ) -> UserAdopters:
        """
        Insert data in user_adopter entity
        :param  - name: name of user_adopter
                - cpf: cpf of user_adopter
                - email: email of user_adopter
                - phone_number: phone_number of user_adopter
                - address_id: id of address (FK)
        :return - tuble with new user_adopter inserted
        """
        created_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                new_user_adopter = UserAdoptersModel(
                    name=name,
                    cpf=cpf,
                    email=email,
                    phone_number=phone_number,
                    address_id=address_id,
                    pet_id=pet_id,
                    created_at=created_at,
                    updated_at=created_at,
                    deleted_at=None
                )
                db_connection.session.add(new_user_adopter)
                self.log.info(f"Inserting new user_adopter: {name}, CPF: {cpf}, Email: {email}, Phone Number: {phone_number}")

                db_connection.session.commit()
                self.log.info(f"New user_adopter inserted with ID: {new_user_adopter.id}")

                return UserAdopters(
                    id=new_user_adopter.id,
                    name=new_user_adopter.name,
                    cpf=new_user_adopter.cpf,
                    email=new_user_adopter.email,
                    phone_number=new_user_adopter.phone_number,
                    address_id=new_user_adopter.address_id,
                    pet_id=new_user_adopter.pet_id,
                )

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while inserting user_adopter {name}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after inserting user_adopter.")
        return None



    def select_user_adopter(
        self,
        id: int = None,
        name: str = None,
        cpf: str = None,
        email: str = None,
        phone_number: str = None,
        address_id: int = None,
        pet_id: int = None,
    ) -> List[UserAdopters]:
        """
        Select data into user_adopter entity
        :param  - user_adopter_id: id of user_adopter
                - phone_number: id of owner
        :return - turple with selected user_adopters
        """

        try:
            data_query = None

            if id:
                with DBConnectionHandler() as db_connection:
                    query = db_connection.session.query(UserAdoptersModel).filter_by(id=id).filter_by(deleted_at=None).one()
                    data_query = [query]
                    self.log.info(f"Selected user_adopter with ID: {id}")

            elif pet_id:
                with DBConnectionHandler() as db_connection:
                    query = db_connection.session.query(UserAdoptersModel).filter_by(pet_id=pet_id).filter_by(deleted_at=None).all()
                    data_query = query
                    self.log.info(f"Selected user_adopters for Pet ID: {pet_id}")

            elif address_id:
                with DBConnectionHandler() as db_connection:
                    query = db_connection.session.query(UserAdoptersModel).filter_by(address_id=address_id).filter_by(deleted_at=None).one()
                    data_query = [query]
                    self.log.info(f"Selected user_adopter with Address ID: {address_id}")

            elif name or cpf or email or phone_number:
                with DBConnectionHandler() as db_connection:
                    filters = {}
                    if name:
                        filters["name"] = name
                        self.log.info(f"Filtering user_adopters by name: {name}")
                    if cpf:
                        filters["cpf"] = cpf
                        self.log.info(f"Filtering user_adopters by CPF: {cpf}")
                    if email:
                        filters["email"] = email
                        self.log.info(f"Filtering user_adopters by email: {email}")
                    if phone_number:
                        filters["phone_number"] = phone_number
                        self.log.info(f"Filtering user_adopters by phone number: {phone_number}")

                    query = db_connection.session.query(UserAdoptersModel).filter_by(**filters).filter_by(deleted_at=None).all()
                    data_query = query
                    self.log.info("Selected user_adopters with provided filters.")

            return data_query

        except NoResultFound:
            self.log.warning("No user_adopters found for the given criteria.")
            return []

        except:
            with DBConnectionHandler() as db_connection:
                db_connection.session.rollback()
                self.log.error("Error occurred while selecting user_adopter, rolling back transaction.")
            raise

        finally:
            with DBConnectionHandler() as db_connection:
                db_connection.session.close()
                self.log.info("Database session closed after selecting user_adopter.")



    def delete_user_adopter(self, id: int) -> bool:
        """
        Delete data from user_adopter entity
        :param  - id: id of the user_adopter to be deleted
        :return - True if the user_adopter was deleted, False otherwise
        """
        deleted_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                user_adopter_to_delete = db_connection.session.query(UserAdoptersModel).filter_by(id=id).filter_by(deleted_at=None).one_or_none()
                self.log.info(f"Attempting to delete user_adopter with ID {id}.")

                if user_adopter_to_delete:
                    user_adopter_to_delete.deleted_at = deleted_at
                    user_adopter_to_delete.updated_at = deleted_at
                    db_connection.session.commit()
                    self.log.info(f"User_adopter with ID {id} deleted successfully.")
                    return True

                self.log.warning(f"User_adopter with ID {id} not found for deletion.")
                return False

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while deleting user_adopter with ID {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after deleting user_adopter.")



    def update_user_adopter(self, id: int, **kwargs: any) -> UserAdopters:
        """
        Update data in user_adopter entity
        :param  - id: id of the user_adopter to be updated
                - **kwargs: dictionary containing fields and their new values
        :return - Updated user_adopter data as an instance of UserAdopters, or None if not found
        """
        updated_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                user_adopter_to_update = db_connection.session.query(UserAdoptersModel).filter_by(id=id).filter_by(deleted_at=None).one_or_none()
                self.log.info(f"Attempting to update user_adopter with ID {id}.")

                if user_adopter_to_update:
                    # Update the params based into kwargs
                    for key, value in kwargs.items():
                        if hasattr(user_adopter_to_update, key):
                            setattr(user_adopter_to_update, key, value)
                            self.log.info(f"Updated {key} for user_adopter ID {id}.")

                    user_adopter_to_update.updated_at = updated_at

                    db_connection.session.commit()
                    self.log.info(f"User_adopter with ID {id} updated successfully.")

                    return UserAdopters(
                        id=user_adopter_to_update.id,
                        name=user_adopter_to_update.name,
                        cpf=user_adopter_to_update.cpf,
                        email=user_adopter_to_update.email,
                        phone_number=user_adopter_to_update.phone_number,
                        address_id=user_adopter_to_update.address_id,
                        pet_id=user_adopter_to_update.pet_id,
                    )

                self.log.warning(f"User_adopter with ID {id} not found for update.")
                return None

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while updating user_adopter with ID {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after updating user_adopter.")
