import logging
from typing import Type, Dict, List
from src.domain.models import Addresses
from src.domain.use_cases import FindAddress as FindAddressInterface
from src.data.interfaces import AddressRepositoryInterface as AddressRepository


class FindAddress(FindAddressInterface):
    """
    Class to define use case Find Address
    """

    def __init__(self, address_repository: Type[AddressRepository]):

        self.address_repository = address_repository

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )



    def by_id(self, id: int) -> Dict[bool, List[Addresses]]:
        """
        Select Address by id
        :param  - id: id from address
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(id, int)
        self.log.info(f"Find Address by id called with id: {id}")

        if validate_entry:
            response = self.address_repository.select_address(id=id)
            self.log.info(f"Address found for id {id}: {response}")

        self.log.info(f"Find Address by id called with id: {id}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}



    def by_complete_discription(
        self,
        cep: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
    ) -> Dict[bool, List[Addresses]]:
        """
        Select Address by complete discription
        :param  - cep: cep from address
                - state: state from address
                - city: city from address
                - neighborhood: neighborhood from address
                - street: street from address
                - number: number from address
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = (
            isinstance(cep, str)
            and isinstance(state, str)
            and isinstance(city, str)
            and isinstance(neighborhood, str)
            and isinstance(street, str)
            and isinstance(number, int)
        )

        if validate_entry:
            response = self.address_repository.select_address(
                cep=cep,
                state=state,
                city=city,
                neighborhood=neighborhood,
                street=street,
                number=number,
            )
            self.log.info(f"Address found for complete description - cep: {cep}, state: {state}, city: {city}, neighborhood: {neighborhood}, street: {street}, number: {number}: {response}")

        self.log.info(f"Find Address by complete description called with cep: {cep}, state: {state}, city: {city}, neighborhood: {neighborhood}, street: {street}, number: {number}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}



    def by_cep_or_state_or_city_or_neighbohood(
        self,
        cep: str = None,
        state: str = None,
        city: str = None,
        neighborhood: str = None,
    ) -> Dict[bool, List[Addresses]]:
        """
        Select Address by cep or state or city or neighborhood
        :param  - cep: cep from address
                - state: state from address
                - city: city from address
                - neighborhood: neighborhood from address
        :return - Dictionary of informations of the process
        """

        response = None
        
        validate_entry = False
        
        if cep or state or city or neighborhood:
            validate_entry = (
                isinstance(cep, (str, type(None)))
                and isinstance(state, (str, type(None)))
                and isinstance(city, (str, type(None)))
                and isinstance(neighborhood, (str, type(None)))
            )
            self.log.info(f"Validation result for find address by cep/state/city/neighborhood: {validate_entry}")
        
        if validate_entry:
            response = self.address_repository.select_address(cep=cep, state=state, city=city, neighborhood=neighborhood)
            self.log.info(f"Address found with provided filters - cep: {cep}, state: {state}, city: {city}, neighborhood: {neighborhood}: {response}")

        self.log.info(f"Find Address by cep/state/city/neighborhood called with cep: {cep}, state: {state}, city: {city}, neighborhood: {neighborhood}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}
