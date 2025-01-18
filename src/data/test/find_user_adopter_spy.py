from typing import Dict, List
from src.domain.models import UserAdopters
from src.domain.test import mock_user_adopter


class FindUserAdopterSpy:
    """
    Class to define usecase: Select UserAdopter
    """

    def __init__(self, user_adopter_repository: any):
        self.user_adopter_repository = user_adopter_repository
        self.by_user_adopter_id_param = {}
        self.by_pet_id_param = {}
        self.by_user_information_param = {}

    def by_user_adopter_id(
        self, user_adopter_id: int
    ) -> Dict[bool, List[UserAdopters]]:
        """
        Select UserAdopter by id
        """

        self.by_user_adopter_id_param["user_adopter_id"] = user_adopter_id
        response = None
        validate_entry = isinstance(user_adopter_id, int)

        if validate_entry:
            response = [mock_user_adopter()]

        return {"Success": validate_entry, "Data": response}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[UserAdopters]]:
        """
        Select UserAdopter by pet_id
        """

        self.by_pet_id_param["pet_id"] = pet_id
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [mock_user_adopter()]

        return {"Success": validate_entry, "Data": response}

    def by_user_information(
        self,
        name: str = None,
        cpf: str = None,
        email: str = None,
        phone_number: str = None,
    ) -> Dict[bool, List[UserAdopters]]:
        """
        Fetch user information based on provided parameters.
        :params:  - name: Name of the user
        :params:  - cpf: CPF of the user
        :params:  - email: Email of the user
        :params:  - phone_number: Phone number of the user
        :return:  - A dictionary containing a success flag and user data
        """

        self.by_user_information_param["name"] = name
        self.by_user_information_param["cpf"] = cpf
        self.by_user_information_param["email"] = email
        self.by_user_information_param["phone_number"] = phone_number

        response = None
        validate_entry = (
            isinstance(name, (str, type(None)))
            or isinstance(cpf, (str, type(None)))
            or isinstance(email, (str, type(None)))
            or isinstance(phone_number, (str, type(None)))
        ) and (
            isinstance(name, str)
            or isinstance(cpf, str)
            or isinstance(email, str)
            or isinstance(phone_number, str)
        )

        if validate_entry:
            response = [mock_user_adopter()]

        return {"Success": validate_entry, "Data": response}
