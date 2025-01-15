from typing import List
from src.domain.test import mock_pet
from src.domain.models import Pets


class PetRepositorySpy:
    """
    Spy for pet repository
    """

    def __init__(self):
        self.insert_pet_param = {}
        self.select_pet_param = {}

    def insert_pet(self, name: str, specie: int, age: int, animal_shelter_id: int, adopted: bool) -> Pets:
        """
        Spy all the attributes
        """

        self.insert_pet_param["name"] = name
        self.insert_pet_param["specie"] = specie
        self.insert_pet_param["age"] = age
        self.insert_pet_param["animal_shelter_id"] = animal_shelter_id
        self.insert_pet_param["adopted"] = adopted

        return mock_pet()

    def select_pet(self, pet_id: int = None, animal_shelter_id: int = None) -> List[Pets]:
        """
        Spy all the attributes
        """

        self.select_pet_param["pet_id"] = pet_id
        self.select_pet_param["animal_shelter_id"] = animal_shelter_id

        return [mock_pet()]
