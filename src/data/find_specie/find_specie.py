# pylint: disable=arguments-differ

from typing import Type, Dict, List
from src.domain.models import Species
from src.domain.use_cases import FindSpecie as FindSpecieInterface
from src.data.interfaces import SpecieRepositoryInterface as SpecieRepository


class FindSpecie(FindSpecieInterface):
    """
    Class to define use case Find Specie
    """

    def __init__(self, specie_repository: Type[SpecieRepository]):

        self.specie_repository = specie_repository

    def by_id(self, id: int) -> Dict[bool, List[Species]]:
        """
        Select Specie by id
        :param  - id: id from specie
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = self.specie_repository.select_specie(id=id)

        return {"Success": validate_entry, "Data": response}

    def by_specie_name(self, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Select Specie by id
        :param  - specie_name: name from specie
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(specie_name, str)

        if validate_entry:
            response = self.specie_repository.select_specie(specie_name=specie_name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_specie_name(self, id: int, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Select Specie by id and specie_name
        :param  - id: id from specie
                - specie_name: name from specie
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(id, int) and isinstance(specie_name, str)

        if validate_entry:
            response = self.specie_repository.select_specie(id=id, specie_name=specie_name)

        return {"Success": validate_entry, "Data": response}
