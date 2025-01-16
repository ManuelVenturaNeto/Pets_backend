from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Addresses


class AddressRepositoryInterface(ABC):
    """
    Interface to Pet Rpository
    """

    @abstractmethod
    def insert_address(cls, cep: int, state: str, city: str, neighborhood: str, street: str, number: int, complement: str = None) -> Addresses:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")

    @abstractmethod
    def select_address(cls, id: int = None, cep: int = None, state: str = None, city: str = None, neighborhood: str = None, street: str = None, number: str = None, complement: str = None) -> List[Addresses]:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")
