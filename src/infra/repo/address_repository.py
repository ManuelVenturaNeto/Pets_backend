# pylint: disable=arguments-differ
# pylint: disable=R0801

from typing import List
from sqlalchemy.exc import NoResultFound
from src.data.interfaces import AddressRepositoryInterface
from src.domain.models import Addresses
from src.infra.config import DBConnectionHandler
from src.infra.entities import Addresses as AddressesModel


class AddressRepository(AddressRepositoryInterface):
    """
    Class to manage Address Repository
    """

    @classmethod
    def insert_address(
        cls,
        cep: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
        complement: str = None,
    ) -> Addresses:
        """
        Insert data in address entity
        :param  - cep: cep of the address owner
                - state: state of the address owner
                - city: city of the address owner
                - neighborhood: id of address owner
                - street: id of address owner
                - number: id of address owner
                - complement: id of address owner if it exists
        :return - tuble with new address inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_address = AddressesModel(
                    cep=cep,
                    state=state,
                    city=city,
                    neighborhood=neighborhood,
                    street=street,
                    number=number,
                    complement=complement,
                )
                db_connection.session.add(new_address)
                db_connection.session.commit()

                return Addresses(
                    id=new_address.id,
                    cep=new_address.cep,
                    state=new_address.state,
                    city=new_address.city,
                    neighborhood=new_address.neighborhood,
                    street=new_address.street,
                    number=new_address.number,
                    complement=new_address.complement,
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
    def select_address(
        cls,
        address_id: int = None,
        cep: str = None,
        state: str = None,
        city: str = None,
        neighborhood: str = None,
        street: str = None,
        number: str = None,
    ) -> List[Addresses]:
        """
        Select data into address entity
        :param  - id: id of address
                - state: state of the address
                - city: city of the address
                - neighborhood: neighborhood of the address
                - street: street of the address
                - number: number of the address
        :return - turple with selected addresses
        """

        try:
            data_query = None

            if address_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AddressesModel)
                        .filter_by(id=address_id)
                        .one()
                    )

                    data_query = [data]

            elif cep and state and city and neighborhood and street and number:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AddressesModel)
                        .filter_by(
                            cep=cep,
                            state=state,
                            city=city,
                            neighborhood=neighborhood,
                            street=street,
                            number=number,
                        )
                        .one()
                    )

                    data_query = [data]

            elif cep or state or city or neighborhood:
                with DBConnectionHandler() as db_connection:

                    filters = {}
                    if cep:
                        filters["cep"] = cep
                    if state:
                        filters["state"] = state
                    if city:
                        filters["city"] = city
                    if neighborhood:
                        filters["neighborhood"] = neighborhood

                    query = db_connection.session.query(AddressesModel).filter_by(
                        **filters
                    )
                    data_query = query.all()

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
    def delete_address(cls, id: int) -> bool:
        """
        Delete data from address entity
        :param  - id: id of the address to be deleted
        :return - True if the address was deleted, False otherwise
        """
        with DBConnectionHandler() as db_connection:
            try:
                address_to_delete = (
                    db_connection.session.query(AddressesModel)
                    .filter_by(id=id)
                    .one_or_none()
                )
                if address_to_delete:
                    db_connection.session.delete(address_to_delete)
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
    def update_address(cls, id: int, **kwargs: any) -> Addresses:
        """
        Update data in address entity
        :param  - id: id of the address to be updated
                - **kwargs: dictionary containing fields and their new values
        :return - Updated address data as an instance of UserAdopters, or None if not found
        """
        with DBConnectionHandler() as db_connection:
            try:
                address_to_update = (
                    db_connection.session.query(AddressesModel)
                    .filter_by(id=id)
                    .one_or_none()
                )
                if address_to_update:
                    # Update params based into kwargs
                    for key, value in kwargs.items():
                        if hasattr(address_to_update, key):
                            setattr(address_to_update, key, value)

                    db_connection.session.commit()

                    return Addresses(
                        id=address_to_update.id,
                        cep=address_to_update.cep,
                        state=address_to_update.state,
                        city=address_to_update.city,
                        neighborhood=address_to_update.neighborhood,
                        street=address_to_update.street,
                        number=address_to_update.number,
                        complement=address_to_update.complement,
                    )
                return None
            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                raise
            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
