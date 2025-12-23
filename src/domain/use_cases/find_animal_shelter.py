from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import AnimalShelters


class FindAnimalShelter(ABC):
    """
    Interface to find animal_shelter
    """

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[AnimalShelters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id")



    @abstractmethod
    def by_name(self, name: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_name")



    @abstractmethod
    def by_id_and_name(self, id: int, name: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id and name")



    @abstractmethod
    def by_cpf(self, cpf: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_cpf")
