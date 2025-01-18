from typing import List
from src.domain.models import AnimalShelters
from src.domain.test import mock_animal_shelter


class AnimalShelterRepositorySpy:
    """
    Spy to AnimalShelter Repository
    """

    def __init__(self):
        self.insert_animal_shelter_params = {}
        self.select_animal_shelter_params = {}

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
        Spy to all the attributes
        """
        self.insert_animal_shelter_params["name"] = name
        self.insert_animal_shelter_params["password"] = password
        self.insert_animal_shelter_params["cpf"] = cpf
        self.insert_animal_shelter_params["responsible_name"] = responsible_name
        self.insert_animal_shelter_params["email"] = email
        self.insert_animal_shelter_params["phone_number"] = phone_number
        self.insert_animal_shelter_params["address_id"] = address_id

        return mock_animal_shelter()

    def select_animal_shelter(
        self,
        id: int = None,
        name: str = None,
        cpf: str = None,
        responsible_name: str = None,
        email: str = None,
        phone_number: str = None,
        address_id: int = None,
    ) -> List[AnimalShelters]:
        """
        Spy to all the attributes
        """
        self.select_animal_shelter_params["id"] = id
        self.select_animal_shelter_params["name"] = name
        self.select_animal_shelter_params["cpf"] = cpf
        self.select_animal_shelter_params["responsible_name"] = responsible_name
        self.select_animal_shelter_params["email"] = email
        self.select_animal_shelter_params["phone_number"] = phone_number
        self.select_animal_shelter_params["address_id"] = address_id

        return [mock_animal_shelter()]
