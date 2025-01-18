from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class RegisterPet(ABC):
    """
    Interface to FindPet use case
    """

    @classmethod
    @abstractmethod
    def register_pet(
        cls,
        name: str,
        specie_name: str,
        animal_shelter_informations: Dict[int, str],
        adopted: bool,
        age: int = None,
    ) -> Dict[bool, Pets]:
        """
        Case
        """

        raise ValueError("Should implement method: register_pet")
