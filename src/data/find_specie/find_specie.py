import logging
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

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )


    def by_id(self, id: int) -> Dict[bool, List[Species]]:
        """
        Select Specie by id
        :param  - id: id from specie
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(id, int)
        self.log.info(f"Find Specie by id called with id: {id}")

        if validate_entry:
            response = self.specie_repository.select_specie(id=id)
            self.log.info(f"Specie found for id {id}: {response}")

        self.log.info(f"Find Specie by id called with id: {id}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}



    def by_specie_name(self, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Select Specie by id
        :param  - specie_name: name from specie
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(specie_name, str)
        self.log.info(f"Find Specie by specie_name called with specie_name: {specie_name}")

        if validate_entry:
            response = self.specie_repository.select_specie(specie_name=specie_name)
            self.log.info(f"Specie found for specie_name {specie_name}: {response}")

        self.log.info(f"Find Specie by specie_name called with specie_name: {specie_name}, Success: {validate_entry}")
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
        self.log.info(f"Find Specie by id and specie_name called with id: {id}, specie_name: {specie_name}")

        if validate_entry:
            response = self.specie_repository.select_specie(id=id, specie_name=specie_name)
            self.log.info(f"Specie found for id {id} and specie_name {specie_name}: {response}")

        self.log.info(f"Find Specie by id and specie_name called with id: {id}, specie_name: {specie_name}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}
