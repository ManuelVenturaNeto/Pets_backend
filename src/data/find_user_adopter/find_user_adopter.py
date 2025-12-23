import logging
from typing import Type, Dict, List
from src.domain.models import UserAdopters
from src.domain.use_cases import FindUserAdopter as FindUserAdopterInterface
from src.data.interfaces import UserAdopterRepositoryInterface as UserAdopterRepository


class FindUserAdopter(FindUserAdopterInterface):
    """
    Interface to find user_adopter
    """

    def __init__(self, user_adopter_repository: Type[UserAdopterRepository]):

        self.user_adopter_repository = user_adopter_repository

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )



    def by_user_adopter_id(self, user_adopter_id: int) -> Dict[bool, List[UserAdopters]]:
        """
        Select UserAdopter for User Adopter id
        :param  - user_adopter_id: id of user adopter
        :return - A dictionary of informations of process
        """
        response = None
        validate_entry = isinstance(user_adopter_id, int)
        self.log.info(f"Find UserAdopter by user_adopter_id called with user_adopter_id: {user_adopter_id}")

        if validate_entry:
            response = self.user_adopter_repository.select_user_adopter(id=user_adopter_id)
            self.log.info(f"UserAdopter found for user_adopter_id {user_adopter_id}: {response}")

        self.log.info(f"Find UserAdopter by user_adopter_id called with user_adopter_id: {user_adopter_id}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}



    def by_pet_id(self, pet_id: int) -> Dict[bool, List[UserAdopters]]:
        """
        Select UserAdopter for Pet id
        :param  - pet_id: id of pet
        :return - A dictionary of informations of process
        """
        response = None
        validate_entry = isinstance(pet_id, int)
        self.log.info(f"Find UserAdopter by pet_id called with pet_id: {pet_id}")

        if validate_entry:
            response = self.user_adopter_repository.select_user_adopter(pet_id=pet_id)
            self.log.info(f"UserAdopter found for pet_id {pet_id}: {response}")

        self.log.info(f"Find UserAdopter by pet_id called with pet_id: {pet_id}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}



    def by_user_information(
        self,
        name: str = None,
        cpf: str = None,
        email: str = None,
        phone_number: str = None,
    ) -> Dict[bool, List[UserAdopters]]:
        """
        Fetch user information based on provided parameters.
        :params:  - name: Name of the user
        :params:  - cpf: CPF of the user
        :params:  - email: Email of the user
        :params:  - phone_number: Phone number of the user
        :return:  - A dictionary containing a success flag and user data
        """
        response = None
        validate_entry = (
            isinstance(name, (str, type(None)))
            or isinstance(cpf, (int, type(None)))
            or isinstance(email, (str, type(None)))
            or isinstance(phone_number, (int, type(None)))
        ) and (
            isinstance(name, str)
            or isinstance(cpf, str)
            or isinstance(email, str)
            or isinstance(phone_number, str)
        )
        self.log.info(f"Find UserAdopter by user information called with name: {name}, cpf: {cpf}, email: {email}, phone_number: {phone_number}")

        if validate_entry:
            response = self.user_adopter_repository.select_user_adopter(
                name=name, 
                cpf=cpf, 
                email=email, 
                phone_number=phone_number
            )
            self.log.info(f"UserAdopter found for provided information: {response}")

        self.log.info(f"Find UserAdopter by user information called with name: {name}, cpf: {cpf}, email: {email}, phone_number: {phone_number}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}
