from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Addresses


class FindAddress(ABC):
    """
    Interface to find animal_shelter
    """

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[Addresses]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id")



    @abstractmethod
    def by_complete_discription(
        self,
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



    @abstractmethod
    def by_cep_or_state_or_city_or_neighbohood(
        self,
        cep: str = None,
        state: str = None,
        city: str = None,
        neighborhood: str = None,
    ) -> Dict[bool, List[Addresses]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_cep_or_state_or_city_or_neighbohood")
