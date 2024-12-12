from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUser(ABC):
    """
    Interface to RegisterUser use case
    """

    @classmethod
    @abstractmethod
    def register_user(cls, name: str, password: str) -> Dict[bool, Users]:
        """
        Case
        """
        raise ValueError("Should implement method: register_user")
