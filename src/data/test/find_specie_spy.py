from typing import Dict, List
from src.domain.models import Species
from src.domain.test import mock_specie


class FindSpecieSpy:
    """
    Class to define usecase: Select Specie
    """

    def __init__(self, specie_repository: any):
        self.specie_repository = specie_repository
        self.by_id_param = {}
        self.by_specie_name_param = {}
        self.by_id_and_specie_name_param = {}

    def by_id(self, id: int) -> Dict[bool, List[Species]]:
        """
        Select Specie by id
        """

        self.by_id_param["id"] = id
        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = [mock_specie()]

        return {"Success": validate_entry, "Data": response}

    def by_specie_name(self, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Select Specie by id
        :param  - specie_name: name from specie
        :return - Dictionary of informations of the process
        """

        self.by_specie_name_param["specie_name"] = specie_name
        response = None
        validate_entry = isinstance(specie_name, str)

        if validate_entry:
            response = [mock_specie()]

        return {"Success": validate_entry, "Data": response}

    def by_id_and_specie_name(self, id: int, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Select Specie by id and specie_name
        :param  - id: id from specie
                - specie_name: name from specie
        :return - Dictionary of informations of the process
        """

        self.by_id_and_specie_name_param["id"] = id
        self.by_id_and_specie_name_param["specie_name"] = specie_name
        response = None
        validate_entry = isinstance(id, int) and isinstance(specie_name, str)

        if validate_entry:
            response = [mock_specie()]

        return {"Success": validate_entry, "Data": response}
