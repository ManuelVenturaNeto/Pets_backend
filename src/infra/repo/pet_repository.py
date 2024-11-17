from src.domain.models import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel


class PetRepository:
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
