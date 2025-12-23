from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Species


class RegisterSpecie(ABC):
    """
    Interface to RegisterSpecie use case
    """

    @abstractmethod
    def register_specie(self, specie_name: str) -> Dict[bool, Species]:
        """
        Case
        """
        raise ValueError("Should implement method: register_specie")