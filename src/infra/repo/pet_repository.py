# pylint: disable=arguments-differ

from typing import List
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel


class PetRepository(PetRepositoryInterface):
    """
    Class to manage Pet Repository
    """

    @classmethod
    def insert_pet(cls, name: str, species: str, age: int, user_id: int) -> Pets:
        """
        Insert data in pet entity
        :param  - name: name of animal
                - species: enum with specie acepted
                - age: age of animal
                - user_id: id of pet owner (FK)
        :return - tuble with new pet inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(
                    name=name, species=species, age=age, user_id=user_id
                )
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    species=new_pet.species.name,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """
        , name: str, species: int, age:int
        Select data into pet entity
        :param  - pet_id: id of pet
                - user_id: id of owner
        :return - turple with selected pets
        """

        try:
            data_query = None

            if pet_id and not user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id)
                        .one()
                    )
                    data.species = data.species.name
                    data_query = [data]

            elif not pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    for pets in data:
                        pets.species = pets.species.name
                    data_query = data

            elif pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    data.species = data.species.name
                    data_query = [data]

            return data_query

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
        return None
