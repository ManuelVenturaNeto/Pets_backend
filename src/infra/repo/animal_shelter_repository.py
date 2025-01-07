# pylint: disable=arguments-differ
# pylint: disable=R0801

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

    @classmethod
    def insert_animal_shelter(cls, name: str, password: str, cpf: int, responsible_name: str, email: str, phone_number: int, address_id: int) -> AnimalShelters:
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

        with DBConnectionHandler() as db_connection:
            try:
                new_animal_shelter = AnimalSheltersModel(name=name, password=password, cpf=cpf, responsible_name=responsible_name, email=email, phone_number=phone_number, address_id=address_id)
                db_connection.session.add(new_animal_shelter)
                db_connection.session.commit()

                return AnimalShelters(
                    id=new_animal_shelter.id, 
                    name=new_animal_shelter.name, 
                    password=new_animal_shelter.password, 
                    cpf=new_animal_shelter.cpf, 
                    responsible_name=new_animal_shelter.responsible_name, 
                    email=new_animal_shelter.email, 
                    phone_number=new_animal_shelter.phone_number, 
                    address_id=new_animal_shelter.address_id
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_animal_shelter(cls, animal_shelter_id: int = None, name: str = None) -> List[AnimalShelters]:
        """
        Select dada in animal_shelter entity by id and/or name
        :param  - animal_shelter_id: id of the register
                - name: AnimalShelter name
        :return - List with AnimalShelters selected
        """

        try:
            query_data = None

            if animal_shelter_id and not name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AnimalSheltersModel)
                        .filter_by(id=animal_shelter_id)
                        .one()
                    )
                    query_data = [data]

            elif not animal_shelter_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AnimalSheltersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif animal_shelter_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AnimalSheltersModel)
                        .filter_by(id=animal_shelter_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise

        finally:
            db_connection.session.close()
