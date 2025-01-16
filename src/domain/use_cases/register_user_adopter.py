from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import UserAdopters


class RegisterUserAdopter(ABC):
    """
    Interface to RegisterUserAdopter use case
    """

    @classmethod
    @abstractmethod
    def register_user_adopter(cls, name: str, cpf: int, pet_id: int, email: str, phone_number: int, cep: int, state: str, city: str, neighborhood: str, street: str, number: int, complement: str = None) -> Dict[bool, UserAdopters]:
        """
        Case
        """
        raise ValueError("Should implement method: register_user_adopter")