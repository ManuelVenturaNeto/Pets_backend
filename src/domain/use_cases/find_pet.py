from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPet(ABC):
    """
    Interface to find Pet
    """

    @classmethod
    @abstractmethod
    def by_pet_id(cls, pet_id: int) -> Dict[bool, List[Pets]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_pet_id")



    @classmethod
    @abstractmethod
    def by_animal_shelter_id(cls, animal_shelter_id: int) -> Dict[bool, List[Pets]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: animal_shelter_id")



    @classmethod
    @abstractmethod
    def by_pet_id_and_animal_shelter_id(cls, pet_id: int, animal_shelter_id: int) -> Dict[bool, List[Pets]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_pet_id and animal_shelter_id")
