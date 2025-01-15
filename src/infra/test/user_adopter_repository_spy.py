from typing import List
from src.domain.models import UserAdopters
from src.domain.test import mock_user_adopter


class UserAdopterRepositorySpy():
    """
    Spy to UserAdopter Repository
    """

    def __init__(self):
        self.insert_user_adopter_params = {}
        self.select_user_adopter_params = {}

    def insert_user_adopter(self, name: str, cpf: str, email: str, phone_number: int, address_id: int, pet_id: int) -> UserAdopters:
        """
        Spy to all the attributes
        """
        self.insert_user_adopter_params["name"] = name
        self.insert_user_adopter_params["cpf"] = cpf
        self.insert_user_adopter_params["email"] = email
        self.insert_user_adopter_params["phone_number"] = phone_number
        self.insert_user_adopter_params["address_id"] = address_id
        self. insert_user_adopter_params["pet_id"] = pet_id

        return mock_user_adopter()

    def select_user_adopter(self, id: int = None, name: str = None, cpf: str = None, email: str = None, phone_number: int = None, address_id: int = None, pet_id: int = None) -> List[UserAdopters]:
        """
        Spy to all the attributes
        """
        self.select_user_adopter_params["id"] = id
        self.select_user_adopter_params["name"] = name
        self.select_user_adopter_params["cpf"] = cpf
        self.select_user_adopter_params["email"] = email
        self.select_user_adopter_params["phone_number"] = phone_number
        self.select_user_adopter_params["address_id"] = address_id
        self. select_user_adopter_params["pet_id"] = pet_id

        return [mock_user_adopter()]
