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
    def insert_animal_shelter(
        cls,
        name: str,
        password: str,
        cpf: str,
        responsible_name: str,
        email: str,
        phone_number: str,
        address_id: int,
    ) -> AnimalShelters:
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
                new_animal_shelter = AnimalSheltersModel(
                    name=name,
                    password=password,
                    cpf=cpf,
                    responsible_name=responsible_name,
                    email=email,
                    phone_number=phone_number,
                    address_id=address_id,
                )
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
                    address_id=new_animal_shelter.address_id,
                )
            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()

        return None

    @classmethod
    def select_animal_shelter(
        cls, id: int = None, name: str = None, cpf: str = None, address_id: int = None
    ) -> List[AnimalShelters]:
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
                    data = (
                        db_connection.session.query(AnimalSheltersModel)
                        .filter_by(id=id)
                        .one()
                    )
                    query_data = [data]

            elif not id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AnimalSheltersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AnimalSheltersModel)
                        .filter_by(id=id, name=name)
                        .one()
                    )
                    query_data = [data]

            elif cpf:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AnimalSheltersModel)
                        .filter_by(cpf=cpf)
                        .one()
                    )
                    query_data = [data]

            elif address_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AnimalSheltersModel)
                        .filter_by(address_id=address_id)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except NoResultFound:
            return []
        except:
            with DBConnectionHandler() as db_connection:
                db_connection.session.rollback()
            raise

        finally:
            with DBConnectionHandler() as db_connection:
                db_connection.session.close()

    @classmethod
    def delete_animal_shelter(cls, id: int) -> bool:
        """
        Delete data from animal_shelter entity
        :param  - id: id of the animal_shelter to be deleted
        :return - True if the animal_shelter was deleted, False otherwise
        """
        with DBConnectionHandler() as db_connection:
            try:
                animal_shelter_to_delete = (
                    db_connection.session.query(AnimalSheltersModel)
                    .filter_by(id=id)
                    .one_or_none()
                )
                if animal_shelter_to_delete:
                    db_connection.session.delete(animal_shelter_to_delete)
                    db_connection.session.commit()
                    return True
                return False
            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                raise
            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()

    @classmethod
    def update_animal_shelter(cls, id: int, **kwargs) -> AnimalShelters:
        """
        Update data in user_adopter entity
        :param  - id: id of the user_adopter to be updated
                - **kwargs: dictionary containing fields and their new values
        :return - Updated user_adopter data as an instance of UserAdopters, or None if not found
        """
        with DBConnectionHandler() as db_connection:
            try:
                animal_shelter_to_update = (
                    db_connection.session.query(AnimalSheltersModel)
                    .filter_by(id=id)
                    .one_or_none()
                )
                if animal_shelter_to_update:
                    # Atualiza os parâmetros com base no kwargs
                    for key, value in kwargs.items():
                        if hasattr(animal_shelter_to_update, key):
                            setattr(animal_shelter_to_update, key, value)

                    db_connection.session.commit()

                    # Certifica-se de passar todos os campos obrigatórios
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
                raise
            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
