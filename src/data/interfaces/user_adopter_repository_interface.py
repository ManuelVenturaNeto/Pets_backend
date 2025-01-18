from abc import ABC, abstractmethod
from typing import List
from src.domain.models import UserAdopters


class UserAdopterRepositoryInterface(ABC):
    """
    Interface to Pet Rpository
    """

    @abstractmethod
    def insert_user_adopter(
        self,
        name: str,
        cpf: str,
        email: str,
        phone_number: str,
        address_id: int,
        pet_id: int,
    ) -> UserAdopters:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")

    @abstractmethod
    def select_user_adopter(
        self,
        id: int = None,
        name: str = None,
        cpf: str = None,
        email: str = None,
        phone_number: str = None,
        address_id: int = None,
        pet_id: int = None,
    ) -> List[UserAdopters]:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")
