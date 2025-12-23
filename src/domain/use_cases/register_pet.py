from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class RegisterPet(ABC):
    """
    Interface to FindPet use case
    """

    @abstractmethod
    def register_pet(
        self,
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
