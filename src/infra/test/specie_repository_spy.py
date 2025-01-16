from typing import List
from src.domain.models import Species
from src.domain.test import mock_specie


class SpecieRepositorySpy:
    """
    Spy to Specie Repository
    """

    def __init__(self):
        self.insert_specie_params = {}
        self.select_specie_params = {}

    def insert_specie(self, specie_name: str) -> Species:
        """
        Spy to all the attributes
        """
        self.insert_specie_params["specie_name"] = specie_name

        return mock_specie()

    def select_specie(self, id: int = None, specie_name: str = None) -> List[Species]:
        """
        Spy to all the attributes
        """
        self.select_specie_params["id"] = id
        self.select_specie_params["specie_name"] = specie_name

        return [mock_specie()]
