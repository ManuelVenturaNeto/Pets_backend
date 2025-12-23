from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Addresses


class RegisterAddress(ABC):
    """
    Interface to RegisterAddress use case
    """

    @abstractmethod
    def register_address(
        self,
        cep: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
        complement: str = None,
    ) -> Dict[bool, Addresses]:
        """
        Case
        """

        raise ValueError("Should implement method: register_address")
