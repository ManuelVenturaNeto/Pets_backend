from typing import Dict, List
from src.domain.models import Pets
from src.domain.test import mock_pets


class FindPetSpy:
    """
    Class to define usecase: Select Pet
    """

    def __init__(self, animal_shelter_repository: any):
        self.pet_repository = animal_shelter_repository
        self.by_pet_id_param = {}
        self.by_animal_shelter_id_param = {}
        self.by_pet_id_and_animal_shelter_id_param = {}

    def by_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """
        Select Pet by id of pet
        """

        self.by_pet_id_param["pet_id"] = pet_id
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"Success": validate_entry, "Data": response}

    def by_animal_shelter_id(self, animal_shelter_id: str) -> Dict[bool, List[Pets]]:
        """
        Select pet by animal_shelter_id
        """

        self.by_animal_shelter_id_param["animal_shelter_id"] = animal_shelter_id
        response = None
        validate_entry = isinstance(animal_shelter_id, str)

        if validate_entry:
            response = [mock_pets()]

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_animal_shelter_id(
        self, pet_id: int, animal_shelter_id: int
    ) -> Dict[bool, List[Pets]]:
        """
        Select AnimalShelter by pet_id and pet_id
        """

        self.by_pet_id_and_animal_shelter_id_param["pet_id"] = pet_id
        self.by_pet_id_and_animal_shelter_id_param["animal_shelter_id"] = animal_shelter_id
        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(animal_shelter_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"Success": validate_entry, "Data": response}
