from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Species


class FindSpecie(ABC):
    """
    Interface to find specie
    """

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[Species]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id")



    @abstractmethod
    def by_specie_name(self, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_specie_name")



    @abstractmethod
    def by_id_and_specie_name(self, id: int, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id_and_specie_name")
