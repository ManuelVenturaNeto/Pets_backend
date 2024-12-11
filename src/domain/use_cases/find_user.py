from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Users


class FindUser(ABC):
    """
    Interface to find user
    """

    @classmethod
    @abstractmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[Users]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id")

    @classmethod
    @abstractmethod
    def by_name(cls, name: str) -> Dict[bool, List[Users]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_name")

    @classmethod
    @abstractmethod
    def by_id_and_name(cls, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """
        Specific Case
        """
        raise ValueError("Should implement method: by_id and name")
