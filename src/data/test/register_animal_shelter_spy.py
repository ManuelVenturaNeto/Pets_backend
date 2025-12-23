from typing import Dict
from src.domain.models import AnimalShelters
from src.domain.test import mock_animal_shelter


class RegisterAnimalShelterSpy:
    """
    Class to define usecase: Register AnimalShelter
    """

    def __init__(self, animal_shelter_repository: any, register_address_service: any):
        self.animal_shelter_repository = animal_shelter_repository
        self.register_address_service = register_address_service
        self.register_param = {}



    def register_animal_shelter(
        self,
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
        Register animal_shelter
        """

        self.register_param["name"] = name
        self.register_param["password"] = password
        self.register_param["cpf"] = cpf
        self.register_param["responsible_name"] = responsible_name
        self.register_param["email"] = email
        self.register_param["phone_number"] = phone_number
        self.register_param["cep"] = cep
        self.register_param["state"] = state
        self.register_param["city"] = city
        self.register_param["neighborhood"] = neighborhood
        self.register_param["street"] = street
        self.register_param["number"] = number
        self.register_param["complement"] = complement

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = mock_animal_shelter()

        return {"Success": validate_entry, "Data": response}
