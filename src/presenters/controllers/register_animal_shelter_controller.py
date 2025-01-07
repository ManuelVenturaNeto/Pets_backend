# pylint: disable=W0221

from typing import Type
from src.main.interfaces import RouteInterface
from src.domain.use_cases import RegisterAnimalShelter
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterAnimalShelterController(RouteInterface):
    """
    Class to Define route to register_animal_shelter use case
    """

    def __init__(self, register_animal_shelter_use_case: Type[RegisterAnimalShelter]):
        self.register_animal_shelter_use_case = register_animal_shelter_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Method to call use case
        """

        response = None

        if http_request.body:

            required_fields = {
                "name": None,
                "password": None,
                "cpf": None,
                "responsible_name": None,
                "email": None,
                "phone_number": None,
                "cep": None,
                "state": None,
                "city": None,
                "neighborhood": None,
                "street": None,
                "number": None,
                "complement": None,
            }

            optional_fields = {
                "complement": None,
            }

            if all(field in http_request.body for field in required_fields):

                body_data = {field: http_request.body[field] for field in required_fields}

                body_data.update({field: http_request.body.get(field, default) for field, default in optional_fields.items()
                })

                response = self.register_animal_shelter_use_case.register_animal_shelter(
                    **body_data
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no body in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )