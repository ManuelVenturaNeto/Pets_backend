from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """
    Interface to Routes
    """

    @classmethod
    @abstractmethod
    def route(cls, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Defining Route
        """

        raise ValueError("Shold implement method: route")
