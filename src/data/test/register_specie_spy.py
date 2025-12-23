from typing import Dict
from src.domain.models import Species
from src.domain.test import mock_specie


class RegisterSpecieSpy:
    """
    Class to define usecase: Register Specie
    """

    def __init__(self, specie_repository: any):
        self.specie_repository = specie_repository
        self.register_param = {}



    def register_specie(self, specie_name: str) -> Dict[bool, Species]:
        """Register specie"""

        self.register_param["specie_name"] = specie_name

        response = None
        validate_entry = isinstance(specie_name, str)

        if validate_entry:
            response = mock_specie()

        return {"Success": validate_entry, "Data": response}
