from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Species


class SpecieRepositoryInterface(ABC):
    """
    Interface to Pet Rpository
    """

    @abstractmethod
    def insert_specie(self, specie_name: str) -> Species:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")

    @abstractmethod
    def select_specie(self, id: int = None, specie_name: int = None) -> List[Species]:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")
