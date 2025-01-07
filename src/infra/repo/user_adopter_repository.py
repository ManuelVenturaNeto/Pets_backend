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
    Class to manemail UsersAdopter Repository
    """

    @classmethod
    def insert_user_adopter(cls, name: str, cpf: int, email: str, phone_number: int, address_id: int, pet_id: int) -> UserAdopters:
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
                    name=name, cpf=cpf, email=email, phone_number=phone_number, address_id=address_id, pet_id=pet_id
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
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_user_adopter(cls, id: int = None, name: str = None, cpf: int = None, email: str = None, phone_number: int = None, address_id: int = None, pet_id: int = None) -> List[UserAdopters]:
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
                    query = db_connection.session.query(UserAdoptersModel).filter_by(id=id).one()
                    data_query = [query]

            elif name or cpf or email or phone_number or address_id or pet_id:
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
                    if address_id:
                        filters["address_id"] = address_id
                    if pet_id:
                        filters["pet_id"] = pet_id

                    query = db_connection.session.query(UserAdoptersModel).filter_by(**filters).all()
                    data_query = query

            return data_query

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()