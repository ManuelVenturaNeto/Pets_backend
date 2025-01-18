from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import AnimalShelters


class RegisterAnimalShelter(ABC):
    """
    Interface to RegisterAnimalShelter use case
    """

    @classmethod
    @abstractmethod
    def register_animal_shelter(
        cls,
        name: str,
        password: str,
        cpf: str,
        responsible_name: str,
        email: str,
        phone_number: str,
        cep: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
        complement: str = None,
    ) -> Dict[bool, AnimalShelters]:
        """
        Case
        """
        raise ValueError("Should implement method: register_animal_shelter")
