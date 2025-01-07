# pylint: disable=arguments-differ
# pylint: disable=R0801

from typing import List
from sqlalchemy.exc import NoResultFound
from src.data.interfaces import SpecieRepositoryInterface
from src.domain.models import Species
from src.infra.config import DBConnectionHandler
from src.infra.entities import Species as SpeciesModel


class SpecieRepository(SpecieRepositoryInterface):
    """
    Class to manage Specie Repository
    """

    @classmethod
    def insert_specie(cls, specie_name: str) -> Species:
        """
        Insert data in specie entity
        :param  - name: name of specie
        :return - tuble with new specie inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_specie = SpeciesModel(specie_name=specie_name)
                db_connection.session.add(new_specie)
                db_connection.session.commit()

                return Species(
                    id=new_specie.id,
                    specie_name=new_specie.specie_name,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_specie(cls, id: int = None, specie_name: int = None) -> List[Species]:
        """
        Select data into specie entity
        :param  - id: id of specie
                - specie_name: id of owner
        :return - turple with selected species
        """

        try:
            data_query = None

            if id and not specie_name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(SpeciesModel)
                        .filter_by(id=id)
                        .one()
                    )
                    data_query = [data]

            elif not id and specie_name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(SpeciesModel)
                        .filter_by(specie_name=specie_name)
                        .one()
                    )
                    data_query = [data]

            elif id and specie_name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(SpeciesModel)
                        .filter_by(id=id, specie_name=specie_name)
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
