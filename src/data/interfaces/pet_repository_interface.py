from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """
    Interface to Pet Rpository
    """

    @abstractmethod
    def insert_pet(self, name: str, species: str, age: int, user_id: int) -> Pets:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")
