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
        :return - turple with selected specie
        """

        try:
            data_query = None

            if id and not specie_name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(SpeciesModel).filter_by(id=id).one()
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
            with DBConnectionHandler() as db_connection:
                db_connection.session.rollback()
            raise
        finally:
            with DBConnectionHandler() as db_connection:
                db_connection.session.close()

    @classmethod
    def delete_specie(cls, id: int) -> bool:
        """
        Delete data from specie entity
        :param  - id: id of the specie to be deleted
        :return - True if the specie was deleted, False otherwise
        """
        with DBConnectionHandler() as db_connection:
            try:
                specie_to_delete = (
                    db_connection.session.query(SpeciesModel)
                    .filter_by(id=id)
                    .one_or_none()
                )
                if specie_to_delete:
                    db_connection.session.delete(specie_to_delete)
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
    def update_specie(cls, id: int, new_specie_name: str) -> Species:
        """
        Update data in specie entity
        :param  - id: id of the specie to be updated
                - new_specie_name: new name for the specie
        :return - Updated specie data
        """
        with DBConnectionHandler() as db_connection:
            try:
                specie_to_update = (
                    db_connection.session.query(SpeciesModel)
                    .filter_by(id=id)
                    .one_or_none()
                )
                if specie_to_update:
                    specie_to_update.specie_name = new_specie_name
                    db_connection.session.commit()
                    return Species(
                        id=specie_to_update.id,
                        specie_name=specie_to_update.specie_name,
                    )
                return None
            except:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.rollback()
                raise

            finally:
                with DBConnectionHandler() as db_connection:
                    db_connection.session.close()
