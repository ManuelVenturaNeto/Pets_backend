# pylint: disable=arguments-differ

from typing import Type, Dict, List
from src.domain.models import Pets
from src.domain.use_cases import FindPet as FindPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository


class FindPet(FindPetInterface):
    """
    Class to define use case Find Pet
    """

    def __init__(self, pet_repository: Type[PetRepository]):

        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id) -> Dict[bool, List[Pets]]:
        """
        Select Pet for Pet id
        :param  - pet_id: id of pet
        :return - A dictionary of informations of process
        """
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: Type[PetRepository]) -> Dict[bool, List[Pets]]:
        """
        Select Pet for User id
        :param  - user_id: id of user
        :return - A dictionary of informations of process
        """

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: Type[PetRepository], user_id: Type[PetRepository]
    ) -> Dict[bool, List[Pets]]:
        """
        Select Pet for Pet id and User id
        :param  - pet_id: id of pet
                - user_id: id of user
        :return - A dictionary of informations of process
        """

        response = None

        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

        return {"Success": validate_entry, "Data": response}
