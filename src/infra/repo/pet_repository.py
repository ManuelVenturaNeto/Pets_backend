# pylint: disable=arguments-differ
# pylint: disable=R0801

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

    @classmethod
    def insert_pet(
        cls, name: str, specie: int, age: int, animal_shelter_id: int, adopted: bool
    ) -> Pets:
        """
        Insert data in pet entity
        :param  - name: name of animal
                - specie: enum with specie acepted
                - age: age of animal
                - animal_shelter_id: id of pet owner (FK)
        :return - tuble with new pet inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(
                    name=name,
                    specie=specie,
                    age=age,
                    animal_shelter_id=animal_shelter_id,
                    adopted=adopted,
                )
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie,
                    age=new_pet.age,
                    animal_shelter_id=new_pet.animal_shelter_id,
                    adopted=new_pet.adopted,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_pet(
        cls, pet_id: int = None, animal_shelter_id: int = None
    ) -> List[Pets]:
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
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id)
                        .one()
                    )
                    data_query = [data]

            elif not pet_id and animal_shelter_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(animal_shelter_id=animal_shelter_id)
                        .all()
                    )
                    data_query = data

            elif pet_id and animal_shelter_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id, animal_shelter_id=animal_shelter_id)
                        .one()
                    )
                    data_query = [data]

            return data_query

        except NoResultFound:
            return []

        except:
            db_connection.session.rollback()
            raise

        finally:
            db_connection.session.close()
