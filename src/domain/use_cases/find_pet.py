from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPet(ABC):
    """
    Interface to find Pet
    """

    @abstractmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_pet_id")



    @abstractmethod
    def by_animal_shelter_id(self, animal_shelter_id: int) -> Dict[bool, List[Pets]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: animal_shelter_id")



    @abstractmethod
    def by_pet_id_and_animal_shelter_id(self, pet_id: int, animal_shelter_id: int) -> Dict[bool, List[Pets]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_pet_id and animal_shelter_id")
