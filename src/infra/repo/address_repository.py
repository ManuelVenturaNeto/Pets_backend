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
    def insert_address(cls, cep: int, state: str, city: str, neighborhood: str, street: str, number: int, complement: str = None) -> Addresses:
        """
        Insert data in address entity
        :param  - cep: cep of the address owner
                - state: state of the address owner
                - city: city of the address owner
                - neighborhood: id of address owner
                - street: id of address owner
                - number: id of address owner
                - complement: id of address owner
        :return - tuble with new address inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_address = AddressesModel(
                    cep=cep, state=state, city=city, neighborhood=neighborhood, street=street, number=number, complement=complement
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
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_address(cls, address_id: int = None, cep: int = None, state: str = None, city: str = None, neighborhood: str = None, street: str = None, number: str = None) -> List[Addresses]:
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
                    data = (db_connection.session.query(AddressesModel).filter_by(id=address_id).one())

                    data_query = [data]

            elif cep and state and city and neighborhood and street and number:
                with DBConnectionHandler() as db_connection:
                    data = (db_connection.session.query(AddressesModel).filter_by(cep=cep, state=state, city=city, neighborhood=neighborhood, street=street, number=number).one())

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

                    query = db_connection.session.query(AddressesModel).filter_by(**filters)
                    data_query = query.all()

            return data_query

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            with DBConnectionHandler() as db_connection:
                db_connection.session.close()
