# pylint: disable=W0221

from typing import Type
from src.main.interfaces import RouteInterface
from src.domain.use_cases import FindAnimalShelter
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindAnimalShelterController(RouteInterface):
    """
    Class to define controller to find_animal_shelter use case
    """

    def __init__(self, find_animal_shelter_use_case: Type[FindAnimalShelter]):
        self.find_animal_shelter_use_case = find_animal_shelter_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Method to call use case
        """

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if (
                "animal_shelter_id" in query_string_params
                and "animal_shelter_name" in query_string_params
            ):
                animal_shelter_id = http_request.query["animal_shelter_id"]
                animal_shelter_name = http_request.query["animal_shelter_name"]
                response = self.find_animal_shelter_use_case.by_id_and_name(
                    id=animal_shelter_id, name=animal_shelter_name
                )

            elif (
                "animal_shelter_id" in query_string_params
                and "animal_shelter_name" not in query_string_params
            ):
                animal_shelter_id = http_request.query["animal_shelter_id"]
                response = self.find_animal_shelter_use_case.by_id(id=animal_shelter_id)

            elif (
                "animal_shelter_id" not in query_string_params
                and "animal_shelter_name" in query_string_params
            ):
                animal_shelter_name = http_request.query["animal_shelter_name"]
                response = self.find_animal_shelter_use_case.by_name(
                    name=animal_shelter_name
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # if no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
