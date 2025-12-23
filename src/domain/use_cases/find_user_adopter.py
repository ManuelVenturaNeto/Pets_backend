from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import UserAdopters


class FindUserAdopter(ABC):
    """
    Interface to find user_adopter
    """

    @abstractmethod
    def by_user_adopter_id(self, user_adopter_id: int) -> Dict[bool, List[UserAdopters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_user_adopter_id")



    @abstractmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[UserAdopters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_pet_id")



    @abstractmethod
    def by_user_information(
        self, name: str, cpf: str, email: str, phone_number: str
    ) -> Dict[bool, List[UserAdopters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_user_information")
