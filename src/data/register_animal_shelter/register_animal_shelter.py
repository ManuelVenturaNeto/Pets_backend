# pylint: disable=arguments-differ

from typing import Dict
import bcrypt
from src.domain.use_cases import RegisterAnimalShelter as RegisterAnimalShelterInterface
from src.data.interfaces import AnimalShelterRepositoryInterface as AnimalShelterRepository
from src.domain.models import AnimalShelters
from src.data.register_address import RegisterAddress


class RegisterAnimalShelter(RegisterAnimalShelterInterface):
    """
    Class to define usecase: Register AnimalShelter
    """

    def __init__(self, animal_shelter_repository: type[AnimalShelterRepository], register_address_service: type[RegisterAddress]):
        self.animal_shelter_repository = animal_shelter_repository
        self.register_address_service = register_address_service

    def register_animal_shelter(self, name: str, password: str, cpf: int, responsible_name: str, email: str, phone_number: int, cep: int, state: str, city: str, neighborhood: str, street: str, number: int, complement: str = None) -> Dict[bool, AnimalShelters]:
        """
        Register animal_shelter usecase
        :param  - name: person name
                - password: password of the person
        :return - Disctionary with informations of the process
        """

        response = None

        validate_entry = isinstance(name, str) and isinstance(password, str) and isinstance(cpf, int) and isinstance(responsible_name, str) and isinstance(email, str) and isinstance(phone_number, int)

        if validate_entry:

            address_response = self.register_address_service.register_address(cep=cep, state=state, city=city, neighborhood=neighborhood, street=street, number=number, complement=complement)

            if address_response["Success"]:
                address_id = address_response["Data"].id
                hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
                response = self.animal_shelter_repository.insert_animal_shelter(name=name, password=hashed_password, cpf=cpf, responsible_name=responsible_name, email=email, phone_number=phone_number, address_id=address_id)

            else:
                validate_entry = False

        return {"Success": validate_entry, "Data": response}
