# pylint: disable=arguments-differ
# pylint: disable=R0801

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

    @classmethod
    def insert_user_adopter(
        cls,
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
        with DBConnectionHandler() as db_connection:
            try:
                new_user_adopter = UserAdoptersModel(
                    name=name,
                    cpf=cpf,
                    email=email,
                    phone_number=phone_number,
                    address_id=address_id,
                    pet_id=pet_id,
                )
                db_connection.session.add(new_user_adopter)
                db_connection.session.commit()

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
                raise
            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
        return None

    @classmethod
    def select_user_adopter(
        cls,
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
                    query = (
                        db_connection.session.query(UserAdoptersModel)
                        .filter_by(id=id)
                        .one()
                    )
                    data_query = [query]

            elif pet_id:
                with DBConnectionHandler() as db_connection:
                    query = (
                        db_connection.session.query(UserAdoptersModel)
                        .filter_by(pet_id=pet_id)
                        .all()
                    )
                    data_query = query

            elif address_id:
                with DBConnectionHandler() as db_connection:
                    query = (
                        db_connection.session.query(UserAdoptersModel)
                        .filter_by(address_id=address_id)
                        .one()
                    )
                    data_query = [query]

            elif name or cpf or email or phone_number:
                with DBConnectionHandler() as db_connection:
                    filters = {}
                    if name:
                        filters["name"] = name
                    if cpf:
                        filters["cpf"] = cpf
                    if email:
                        filters["email"] = email
                    if phone_number:
                        filters["phone_number"] = phone_number

                    query = (
                        db_connection.session.query(UserAdoptersModel)
                        .filter_by(**filters)
                        .all()
                    )
                    data_query = query

            return data_query

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
    def delete_user_adopter(cls, id: int) -> bool:
        """
        Delete data from user_adopter entity
        :param  - id: id of the user_adopter to be deleted
        :return - True if the user_adopter was deleted, False otherwise
        """
        with DBConnectionHandler() as db_connection:
            try:
                user_adopter_to_delete = (
                    db_connection.session.query(UserAdoptersModel)
                    .filter_by(id=id)
                    .one_or_none()
                )
                if user_adopter_to_delete:
                    db_connection.session.delete(user_adopter_to_delete)
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
    def update_user_adopter(cls, id: int, **kwargs: any) -> UserAdopters:
        """
        Update data in user_adopter entity
        :param  - id: id of the user_adopter to be updated
                - **kwargs: dictionary containing fields and their new values
        :return - Updated user_adopter data as an instance of UserAdopters, or None if not found
        """
        with DBConnectionHandler() as db_connection:
            try:
                user_adopter_to_update = (
                    db_connection.session.query(UserAdoptersModel)
                    .filter_by(id=id)
                    .one_or_none()
                )
                if user_adopter_to_update:
                    # Update the params based into kwargs
                    for key, value in kwargs.items():
                        if hasattr(user_adopter_to_update, key):
                            setattr(user_adopter_to_update, key, value)

                    db_connection.session.commit()

                    return UserAdopters(
                        id=user_adopter_to_update.id,
                        name=user_adopter_to_update.name,
                        cpf=user_adopter_to_update.cpf,
                        email=user_adopter_to_update.email,
                        phone_number=user_adopter_to_update.phone_number,
                        address_id=user_adopter_to_update.address_id,
                        pet_id=user_adopter_to_update.pet_id,
                    )
                return None
            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                raise
            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
