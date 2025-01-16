from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import AnimalShelters


class FindAnimalShelter(ABC):
    """
    Interface to find animal_shelter
    """

    @classmethod
    @abstractmethod
    def by_id(cls, animal_shelter_id: int) -> Dict[bool, List[AnimalShelters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id")

    @classmethod
    @abstractmethod
    def by_name(cls, name: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_name")

    @classmethod
    @abstractmethod
    def by_id_and_name(
        cls, animal_shelter_id: int, name: str
    ) -> Dict[bool, List[AnimalShelters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id and name")

    @classmethod
    @abstractmethod
    def by_cpf(cls, cpf: int) -> Dict[bool, List[AnimalShelters]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_cpf")
