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

    def by_animal_shelter_id(
        self, animal_shelter_id: Type[PetRepository]
    ) -> Dict[bool, List[Pets]]:
        """
        Select Pet for AnimalShelter id
        :param  - animal_shelter_id: id of animal_shelter
        :return - A dictionary of informations of process
        """

        response = None

        validate_entry = isinstance(animal_shelter_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(
                animal_shelter_id=animal_shelter_id
            )

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_animal_shelter_id(
        self, pet_id: Type[PetRepository], animal_shelter_id: Type[PetRepository]
    ) -> Dict[bool, List[Pets]]:
        """
        Select Pet for Pet id and AnimalShelter id
        :param  - pet_id: id of pet
                - animal_shelter_id: id of animal_shelter
        :return - A dictionary of informations of process
        """

        response = None

        validate_entry = isinstance(pet_id, int) and isinstance(animal_shelter_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(
                pet_id=pet_id, animal_shelter_id=animal_shelter_id
            )

        return {"Success": validate_entry, "Data": response}
