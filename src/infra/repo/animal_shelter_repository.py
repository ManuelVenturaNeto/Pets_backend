import logging
import datetime
from typing import List
from sqlalchemy.exc import NoResultFound
from src.data.interfaces import AnimalShelterRepositoryInterface
from src.domain.models import AnimalShelters
from src.infra.config import DBConnectionHandler
from src.infra.entities import AnimalShelters as AnimalSheltersModel


class AnimalShelterRepository(AnimalShelterRepositoryInterface):
    """
    Class to manage AnimalShelter Repository
    """

    def __init__(self):

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )


    def insert_animal_shelter(self, name: str, password: str, cpf: str, responsible_name: str, email: str, phone_number: str, address_id: int) -> AnimalShelters:
        """
        insert data in animal_shelter entity
        :param  - name: person name
                - password: animal_shelter password
                - cpf: animal_shelter cpf
                - responsible_name: animal_shelter responsible name
                - email: animal_shelter email
                - phone_number: animal_shelter phone number
                - address_id: id of address (FK)
        :return - tuple with new animal_shelter inserted
        """
        created_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                new_animal_shelter = AnimalSheltersModel(
                    name=name,
                    password=password,
                    cpf=cpf,
                    responsible_name=responsible_name,
                    email=email,
                    phone_number=phone_number,
                    address_id=address_id,
                    created_at=created_at,
                    updated_at=created_at,
                    deleted_at=None,
                )
                db_connection.session.add(new_animal_shelter)
                self.log.info(f"Inserting new animal shelter: {name}, CPF: {cpf}")

                db_connection.session.commit()
                self.log.info(f"Animal shelter {name} inserted successfully with ID: {new_animal_shelter.id}")

                return AnimalShelters(
                    id=new_animal_shelter.id,
                    name=new_animal_shelter.name,
                    password=new_animal_shelter.password,
                    cpf=new_animal_shelter.cpf,
                    responsible_name=new_animal_shelter.responsible_name,
                    email=new_animal_shelter.email,
                    phone_number=new_animal_shelter.phone_number,
                    address_id=new_animal_shelter.address_id,
                )
            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while inserting animal shelter {name}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after inserting animal shelter.")

        return None



    def select_animal_shelter(self, id: int = None, name: str = None, cpf: str = None, address_id: int = None) -> List[AnimalShelters]:
        """
        Select dada in animal_shelter entity by id and/or name
        :param  - id: id of the register
                - name: AnimalShelter name
        :return - List with AnimalShelters selected
        """

        try:
            query_data = None

            if id and not name:

                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(AnimalSheltersModel).filter_by(id=id).filter_by(deleted_at=None).one()
                    query_data = [data]
                    self.log.info(f"Selected animal shelter with id {id}.")

            elif not id and name:

                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(AnimalSheltersModel).filter_by(name=name).filter_by(deleted_at=None).one()
                    query_data = [data]
                    self.log.info(f"Selected animal shelter with name {name}.")

            elif id and name:

                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(AnimalSheltersModel).filter_by(id=id, name=name).filter_by(deleted_at=None).one()
                    query_data = [data]
                    self.log.info(f"Selected animal shelter with id {id} and name {name}.")

            elif cpf:

                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(AnimalSheltersModel).filter_by(cpf=cpf).filter_by(deleted_at=None).one()
                    query_data = [data]
                    self.log.info(f"Selected animal shelter with CPF {cpf}.")

            elif address_id:

                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(AnimalSheltersModel).filter_by(address_id=address_id).filter_by(deleted_at=None).one()
                    query_data = [data]
                    self.log.info(f"Selected animal shelter with address ID {address_id}.")

            return query_data

        except NoResultFound:
            self.log.info("No animal shelter found with the given parameters.")
            return []

        except:
            with DBConnectionHandler() as db_connection:
                db_connection.session.rollback()
                self.log.error("Error occurred while selecting animal shelter, rolling back transaction.")
            raise

        finally:
            with DBConnectionHandler() as db_connection:
                db_connection.session.close()
                self.log.info("Database session closed after selecting animal shelter.")



    def delete_animal_shelter(self, id: int) -> bool:
        """
        Delete data from animal_shelter entity
        :param  - id: id of the animal_shelter to be deleted
        :return - True if the animal_shelter was deleted, False otherwise
        """
        deleted_at = datetime.datetime.now(datetime.timezone.utc)
        
        with DBConnectionHandler() as db_connection:
            try:
                animal_shelter_to_delete = db_connection.session.query(AnimalSheltersModel).filter_by(id=id).filter_by(deleted_at=None).one_or_none()
                self.log.info(f"Attempting to delete animal shelter with id {id}.")

                if animal_shelter_to_delete:
                    animal_shelter_to_delete.deleted_at = deleted_at
                    animal_shelter_to_delete.updated_at = deleted_at
                    db_connection.session.commit()
                    self.log.info(f"Animal shelter with id {id} deleted successfully.")
                    return True

                self.log.info(f"Animal shelter with id {id} not found for deletion.")
                return False

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while deleting animal shelter with id {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after deleting animal shelter.")



    def update_animal_shelter(self, id: int, **kwargs: any) -> AnimalShelters:
        """
        Update data in user_adopter entity
        :param  - id: id of the user_adopter to be updated
                - **kwargs: dictionary containing fields and their new values
        :return - Updated user_adopter data as an instance of UserAdopters, or None if not found
        """
        updated_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                animal_shelter_to_update = db_connection.session.query(AnimalSheltersModel).filter_by(id=id).filter_by(deleted_at=None).one_or_none()
                self.log.info(f"Attempting to update animal shelter with id {id}.")

                if animal_shelter_to_update:
                    # Update params based into kwargs
                    for key, value in kwargs.items():
                        if hasattr(animal_shelter_to_update, key):
                            setattr(animal_shelter_to_update, key, value)
                            self.log.info(f"Updated {key} of animal shelter id {id} to {value}.")

                    animal_shelter_to_update.updated_at = updated_at

                    db_connection.session.commit()
                    self.log.info(f"Animal shelter with id {id} updated successfully.")

                    return AnimalShelters(
                        id=animal_shelter_to_update.id,
                        name=animal_shelter_to_update.name,
                        password=animal_shelter_to_update.password,
                        cpf=animal_shelter_to_update.cpf,
                        responsible_name=animal_shelter_to_update.responsible_name,
                        email=animal_shelter_to_update.email,
                        phone_number=animal_shelter_to_update.phone_number,
                        address_id=animal_shelter_to_update.address_id,
                    )
                return None

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while updating animal shelter with id {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after updating animal shelter.")
