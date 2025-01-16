from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import UserAdopters


class FindUserAdopter(ABC):
    """
    Interface to find user_adopter
    """

    @classmethod
    @abstractmethod
    def by_user_adopter_id(cls, user_adopter_id: int) -> Dict[bool, List[UserAdopters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_user_adopter_id")
    
    @classmethod
    @abstractmethod
    def by_pet_id(cls, pet_id: int) -> Dict[bool, List[UserAdopters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_pet_id")

    @classmethod
    @abstractmethod
    def by_user_information(cls, name: str, cpf: int, email: str, phone_number: int) -> Dict[bool, List[UserAdopters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_user_information")
