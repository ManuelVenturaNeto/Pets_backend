# pylint: disable=W0237, R1701

from typing import Dict, List
from src.domain.test import mock_pets, mock_user
from src.domain.models import Pets, Users


class RegisterPetSpy:
    """
    Class to difine use case register pet
    """

    def __init__(self, pet_repository: any, find_user: any):
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.register_pet_param = {}

    def register_pet(
        self, name: str, species: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """
        Register pet
        """

        self.register_pet_param["name"] = name
        self.register_pet_param["species"] = species
        self.register_pet_param["user_information"] = user_information
        self.register_pet_param["age"] = age

        response = None

        validate_entry = (
            isinstance(name, str)
            and isinstance(species, str)
            and (isinstance(age, int) or isinstance(age, type(None)))
        )

        user = self.__find_user_information(user_information)

        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pets()

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """
        Check user informations
        """

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = {"Success": True, "Data": mock_user()}

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = {"Success": True, "Data": mock_user()}

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = {"Success": True, "Data": mock_user()}

        else:
            return {"Success": False, "Data": None}

        return user_founded
