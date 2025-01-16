# pylint: disable=W0221, W0237

from typing import Type, Dict, List
from src.domain.models import UserAdopters
from src.domain.use_cases import FindUserAdopter as FindUserAdopterInterface
from src.data.interfaces import UserAdopterRepositoryInterface as UserAdopterRepository


class FindUserAdopter(FindUserAdopterInterface):
    """
    Interface to find user_adopter
    """

    def __init__(self, user_adopter_repository: Type[UserAdopterRepository]):

        self.user_adopter_repository = user_adopter_repository

    def by_user_adopter_id(
        self, user_adopter_id: int
    ) -> Dict[bool, List[UserAdopters]]:
        """
        Select UserAdopter for User Adopter id
        :param  - user_adopter_id: id of user adopter
        :return - A dictionary of informations of process
        """
        response = None
        validate_entry = isinstance(user_adopter_id, int)

        if validate_entry:
            response = self.user_adopter_repository.select_user_adopter(
                id=user_adopter_id
            )

        return {"Success": validate_entry, "Data": response}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[UserAdopters]]:
        """
        Select UserAdopter for Pet id
        :param  - pet_id: id of pet
        :return - A dictionary of informations of process
        """
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.user_adopter_repository.select_user_adopter(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_information(
        self,
        name: str = None,
        cpf: int = None,
        email: str = None,
        phone_number: int = None,
    ) -> Dict[bool, List[UserAdopters]]:
        """
        Fetch user information based on provided parameters.
        :params:  - name: Name of the user
        :params:  - cpf: CPF of the user
        :params:  - email: Email of the user
        :params:  - phone_number: Phone number of the user
        :return:  - A dictionary containing a success flag and user data
        """
        response = None
        validate_entry = (
            isinstance(name, (str, type(None)))
            or isinstance(cpf, (int, type(None)))
            or isinstance(email, (str, type(None)))
            or isinstance(phone_number, (int, type(None)))
        ) and (
            isinstance(name, str)
            or isinstance(cpf, str)
            or isinstance(email, str)
            or isinstance(phone_number, str)
        )

        if validate_entry:
            response = self.user_adopter_repository.select_user_adopter(
                name=name, cpf=cpf, email=email, phone_number=phone_number
            )

        return {"Success": validate_entry, "Data": response}
