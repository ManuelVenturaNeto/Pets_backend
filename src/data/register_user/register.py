# pylint: disable=arguments-differ

from typing import Dict
import bcrypt
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Users


class RegisterUser(RegisterUserInterface):
    """
    Class to define usecase: Register User
    """

    def __init__(self, user_repository: type[UserRepository]):
        self.user_repository = user_repository

    def register_user(self, name: str, password: str) -> Dict[bool, Users]:
        """
        Register user usecase
        :param  - name: person name
                - password: password of the person
        :return - Disctionary with informations of the process
        """

        response = None

        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:

            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

            response = self.user_repository.insert_user(name, hashed_password)

        return {"Success": validate_entry, "Data": response}
