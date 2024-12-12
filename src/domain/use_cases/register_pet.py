from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class RegisterPet(ABC):
    """
    Interface to FindPet use case
    """

    @classmethod
    @abstractmethod
    def registrer_pet(
        cls, name: str, species: str, user_informations: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """
        Case
        """

        raise ValueError("Should implement method: register_pet")
