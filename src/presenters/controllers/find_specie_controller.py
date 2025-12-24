import logging
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

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )


    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Method to call use case
        """

        response = None

        if http_request.query_params:
            query_string_params = http_request.query_params.keys()

            if "id" in query_string_params and "specie_name" in query_string_params:
                id = http_request.query_params["id"]
                specie_name = http_request.query_params["specie_name"]
                response = self.find_specie_use_case.by_id_and_specie_name(id=id, specie_name=specie_name)
                self.log.info(f"Finding Specie by ID: {id} and Specie Name: {specie_name}")

            elif (
                "id" in query_string_params
                and "specie_name" not in query_string_params
            ):
                id = http_request.query_params["id"]
                response = self.find_specie_use_case.by_id(id=id)
                self.log.info(f"Finding Specie by ID: {id}")

            elif (
                "id" not in query_string_params
                and "specie_name" in query_string_params
            ):
                specie_name = http_request.query_params["specie_name"]
                response = self.find_specie_use_case.by_specie_name(specie_name=specie_name)
                self.log.info(f"Finding Specie by Specie Name: {specie_name}")

            else:
                response = {"Success": False, "Data": None}
                self.log.warning("Invalid query parameters for finding Specie")

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                self.log.error("Error occurred while finding Specie")
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

            self.log.info("Specie found successfully")
            return HttpResponse(status_code=200, body=response["Data"])

        # if no query in http_request
        http_error = HttpErrors.error_400()
        self.log.error("Bad Request: No query parameters provided")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
