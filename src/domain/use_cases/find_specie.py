from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Species


class FindSpecie(ABC):
    """
    Interface to find specie
    """

    @classmethod
    @abstractmethod
    def by_id(cls, id: int) -> Dict[bool, List[Species]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id")

    @classmethod
    @abstractmethod
    def by_specie_name(cls, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_specie_name")

    @classmethod
    @abstractmethod
    def by_id_and_specie_name(cls, id: int, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id_and_specie_name")
