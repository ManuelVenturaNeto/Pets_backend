from typing import List
from src.domain.models import Addresses
from src.domain.test import mock_address


class AddressRepositorySpy:
    """
    Spy to Address Repository
    """

    def __init__(self):
        self.insert_address_params = {}
        self.select_address_params = {}

    def insert_address(self,cep: int, state: str, city: str, neighborhood: str, street: str, number: int, complement: str = None) -> Addresses:
        """
        Spy to all the attributes
        """
        self.insert_address_params["cep"] = cep
        self.insert_address_params["state"] = state
        self.insert_address_params["city"] = city
        self.insert_address_params["neighborhood"] = neighborhood
        self.insert_address_params["street"] = street
        self.insert_address_params["number"] = number
        self.insert_address_params["complement"] = complement

        return mock_address()

    def select_address(self, id: int = None, cep: int = None, state: str = None, city: str = None, neighborhood: str = None, street: str = None, number: int = None, complement: str = None) -> List[Addresses]:
        """
        Spy to all the attributes
        """
        self.select_address_params["id"] = id
        self.select_address_params["cep"] = cep
        self.select_address_params["state"] = state
        self.select_address_params["city"] = city
        self.select_address_params["neighborhood"] = neighborhood
        self.select_address_params["street"] = street
        self.select_address_params["number"] = number
        self.select_address_params["complement"] = complement

        return [mock_address()]
