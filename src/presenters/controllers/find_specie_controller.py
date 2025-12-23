from typing import Type
from src.main.interfaces import RouteInterface
from src.domain.use_cases import FindSpecie
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindSpecieController(RouteInterface):
    """
    Class to define controller to find_specie use case
    """

    def __init__(self, find_specie_use_case: Type[FindSpecie]):
        self.find_specie_use_case = find_specie_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Method to call use case
        """

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "id" in query_string_params and "specie_name" in query_string_params:
                id = http_request.query["id"]
                specie_name = http_request.query["specie_name"]
                response = self.find_specie_use_case.by_id_and_specie_name(
                    id=id, specie_name=specie_name
                )

            elif (
                "id" in query_string_params
                and "specie_name" not in query_string_params
            ):
                id = http_request.query["id"]
                response = self.find_specie_use_case.by_id(id=id)

            elif (
                "id" not in query_string_params
                and "specie_name" in query_string_params
            ):
                specie_name = http_request.query["specie_name"]
                response = self.find_specie_use_case.by_specie_name(specie_name=specie_name)

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
