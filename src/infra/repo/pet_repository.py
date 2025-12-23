import logging
import datetime
from typing import List
from sqlalchemy.exc import NoResultFound
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel


class PetRepository(PetRepositoryInterface):
    """
    Class to manage Pet Repository
    """

    def __init__(self):

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )


    def insert_pet(self, name: str, specie: int, age: int, animal_shelter_id: int, adopted: bool) -> Pets:
        """
        Insert data in pet entity
        :param  - name: name of animal
                - specie: enum with specie acepted
                - age: age of animal
                - animal_shelter_id: id of pet owner (FK)
        :return - tuble with new pet inserted
        """
        created_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(
                    name=name,
                    specie=specie,
                    age=age,
                    animal_shelter_id=animal_shelter_id,
                    adopted=adopted,
                    created_at=created_at,
                    updated_at=created_at,
                    deleted_at=None,
                )
                db_connection.session.add(new_pet)
                self.log.info(f"Inserting new pet: {name}, Specie: {specie}, Age: {age}, Animal Shelter ID: {animal_shelter_id}")

                db_connection.session.commit()
                self.log.info(f"New pet inserted with ID: {new_pet.id}")

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie,
                    age=new_pet.age,
                    animal_shelter_id=new_pet.animal_shelter_id,
                    adopted=new_pet.adopted,
                )

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                self.log.error("Error occurred while inserting new pet, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after inserting pet.")
        return None



    def select_pet(self, pet_id: int = None, animal_shelter_id: int = None) -> List[Pets]:
        """
        Select data into pet entity
        :param  - pet_id: id of pet
                - animal_shelter_id: id of owner
        :return - turple with selected pets
        """

        try:
            data_query = None

            if pet_id and not animal_shelter_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsModel).filter_by(id=pet_id).one()
                    data_query = [data]
                    self.log.info(f"Selected pet with ID: {pet_id}")

            elif not pet_id and animal_shelter_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsModel).filter_by(animal_shelter_id=animal_shelter_id).all()
                    data_query = data
                    self.log.info(f"Selected pets for Animal Shelter ID: {animal_shelter_id}")

            elif pet_id and animal_shelter_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsModel).filter_by(id=pet_id, animal_shelter_id=animal_shelter_id).one()
                    data_query = [data]
                    self.log.info(f"Selected pet with ID: {pet_id} for Animal Shelter ID: {animal_shelter_id}")

            return data_query

        except NoResultFound:
            self.log.warning("No pets found for the given criteria.")
            return []

        except:
            with DBConnectionHandler() as db_connection:
                db_connection.session.rollback()
                self.log.error("Error occurred while selecting pets, rolling back transaction.")
            raise

        finally:
            with DBConnectionHandler() as db_connection:
                db_connection.session.close()
                self.log.info("Database session closed after selecting pets.")



    def delete_pet(self, id: int) -> bool:
        """
        Delete data from pet entity
        :param  - id: id of the pet to be deleted
        :return - True if the pet was deleted, False otherwise
        """
        deleted_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                pet_to_delete = db_connection.session.query(PetsModel).filter_by(id=id).one_or_none()

                if pet_to_delete:
                    pet_to_delete.deleted_at = deleted_at
                    pet_to_delete.updated_at = deleted_at
                    db_connection.session.commit()
                    self.log.info(f"Pet with ID {id} deleted successfully.")
                    return True

                self.log.warning(f"Pet with ID {id} not found for deletion.")
                return False

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while deleting pet with ID {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after deleting pet.")



    def update_pet(self, id: int, **kwargs: any) -> Pets:
        """
        Update data in pet entity
        :param  - id: id of the pet to be updated
                - **kwargs: dictionary containing fields and their new values
        :return - Updated pet data as an instance of UserAdopters, or None if not found
        """
        updated_at = datetime.datetime.now(datetime.timezone.utc)

        with DBConnectionHandler() as db_connection:
            try:
                pet_to_update = db_connection.session.query(PetsModel).filter_by(id=id).one_or_none()
                self.log.info(f"Attempting to update pet with ID {id}.")

                if pet_to_update:
                    # Update the params based into kwrgs
                    for key, value in kwargs.items():
                        if hasattr(pet_to_update, key):
                            setattr(pet_to_update, key, value)
                            self.log.info(f"Updated {key} for pet ID {id} to {value}.")

                    pet_to_update.updated_at = updated_at

                    db_connection.session.commit()
                    self.log.info(f"Pet with ID {id} updated successfully.")

                    return PetsModel(
                        id=pet_to_update.id,
                        name=pet_to_update.name,
                        specie=pet_to_update.specie,
                        age=pet_to_update.age,
                        animal_shelter_id=pet_to_update.animal_shelter_id,
                        adopted=pet_to_update.adopted,
                    )
                self.log.warning(f"Pet with ID {id} not found for update.")
                return None

            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                    self.log.error(f"Error occurred while updating pet with ID {id}, rolling back transaction.")
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
                    self.log.info("Database session closed after updating pet.")
