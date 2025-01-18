from typing import Dict
from src.domain.models import UserAdopters
from src.domain.test import mock_user_adopter


class RegisterUserAdopterSpy:
    """Class to define usecase: Register UserAdopter"""

    def __init__(self, user_adopter_repository: any, register_address_service: any):
        self.user_adopter_repository = user_adopter_repository
        self.register_address_service = register_address_service
        self.register_param = {}

    def register_user_adopter(
        self,
        name: str,
        cpf: str,
        email: str,
        phone_number: str,
        pet_id,
        cep: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
        complement: str = None,
    ) -> Dict[bool, UserAdopters]:
        """Register user_adopter"""

        self.register_param["name"] = name
        self.register_param["cpf"] = cpf
        self.register_param["email"] = email
        self.register_param["phone_number"] = phone_number
        self.register_param["pet_id"] = pet_id
        self.register_param["cep"] = cep
        self.register_param["state"] = state
        self.register_param["city"] = city
        self.register_param["neighborhood"] = neighborhood
        self.register_param["street"] = street
        self.register_param["number"] = number
        self.register_param["complement"] = complement

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(cpf, str)
            and isinstance(email, str)
            and isinstance(phone_number, str)
            and isinstance(pet_id, int)
        )

        if validate_entry:
            response = mock_user_adopter()

        return {"Success": validate_entry, "Data": response}
