from abc import ABC, abstractmethod
from typing import List
from src.domain.models import UserAdopters


class UserAdopterRepositoryInterface(ABC):
    """
    Interface to Pet Rpository
    """

    @abstractmethod
    def insert_user_adopter(self, name: str, cpf: int, email: str, phone_number: int, address_id: int, pet_id: int) -> UserAdopters:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")

    @abstractmethod
    def select_user_adopter(self, id: int = None, name: str = None, cpf: int = None, email: str = None, phone_number: int = None, address_id: int = None, pet_id: int = None) -> List[UserAdopters]:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")
