from abc import ABC, abstractmethod
from typing import List
from src.domain.models import AnimalShelters


class AnimalShelterRepositoryInterface(ABC):
    """
    Interface to AnimalShelter Rpository
    """

    @abstractmethod
    def insert_animal_shelter(
        self,
        name: str,
        password: str,
        cpf: str,
        responsible_name: str,
        email: str,
        phone_number: str,
        address_id: int,
    ) -> AnimalShelters:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")

    @abstractmethod
    def select_animal_shelter(
        self, id: int = None, name: str = None, cpf: str = None
    ) -> List[AnimalShelters]:
        """
        Abstractmethod
        """
        raise ValueError("Method not implemented")
