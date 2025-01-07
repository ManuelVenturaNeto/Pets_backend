# pylint: disable=arguments-differ

from typing import Dict
from src.domain.use_cases import RegisterAddress as RegisterAddressInterface
from src.data.interfaces import AddressRepositoryInterface as AddressRepository
from src.domain.models import Addresses


class RegisterAddress(RegisterAddressInterface):
    """
    Class to define usecase: Register Address
    """

    def __init__(self, address_repository: type[AddressRepository]):
        self.address_repository = address_repository

    def register_address(self, cep: int, state: str, city: str, neighborhood: str, street: str, number: int, complement: str = None) -> Dict[bool, Addresses]:
        """
        Register address usecase
        :param  - cep: person cep
                - state: state of the person
                - city: city of the person
                - neighborhood: neighborhood of the person
                - street: street of the person
                - complement: complement of the person
                - number: number of the person
        :return - Disctionary with informations of the process
        """

        response = None

        validate_entry = isinstance(cep, int) and isinstance(state, str) and isinstance(city, str) and isinstance(neighborhood, str) and isinstance(street, str) and isinstance(number, int)and (isinstance(complement, str) or isinstance(complement, type(None)))

        if validate_entry:
            response = self.address_repository.insert_address(cep=cep, state=state, city=city, neighborhood=neighborhood, street=street, number=number, complement=complement)

        return {"Success": validate_entry, "Data": response}
