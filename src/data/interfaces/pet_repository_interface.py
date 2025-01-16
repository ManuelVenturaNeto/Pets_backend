from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """
    Interface to Pet Rpository
    """

    @abstractmethod
    def insert_pet(self, name: str, specie: int, age: int, animal_shelter_id: int, adopted: bool) -> Pets:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")

    @abstractmethod
    def select_pet(self, pet_id: int = None, animal_shelter_id: int = None) -> List[Pets]:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")
