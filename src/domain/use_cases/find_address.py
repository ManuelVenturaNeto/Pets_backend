from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Addresses


class FindAddress(ABC):
    """
    Interface to find animal_shelter
    """

    @classmethod
    @abstractmethod
    def by_id(cls, id: int) -> Dict[bool, List[Addresses]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id")

    @classmethod
    @abstractmethod
    def by_complete_discription(
        cls,
        cep: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
    ) -> Dict[bool, List[Addresses]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_complete_discription")

    @classmethod
    @abstractmethod
    def by_cep_or_state_or_city_or_neighbohood(
        cls,
        cep: str = None,
        state: str = None,
        city: str = None,
        neighborhood: str = None,
    ) -> Dict[bool, List[Addresses]]:
        """
        Specific Case
        """
        raise ValueError(
            "Should implement method: by_cep_or_state_or_city_or_neighbohood"
        )
