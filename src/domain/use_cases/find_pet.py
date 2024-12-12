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
    def by_user_id(cls, user_id: int) -> Dict[bool, List[Pets]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: user_id")

    @classmethod
    @abstractmethod
    def by_pet_id_and_user_id(cls, pet_id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_pet_id and user_id")
