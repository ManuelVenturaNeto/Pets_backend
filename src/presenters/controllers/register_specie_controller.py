import logging
from typing import Type
from src.main.interfaces import RouteInterface
from src.domain.use_cases import RegisterSpecie
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterSpecieController(RouteInterface):
    """
    Class to Define route to register_specie use case
    """

    def __init__(self, register_specie_use_case: Type[RegisterSpecie]):
        self.register_specie_use_case = register_specie_use_case

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

        if http_request.body:
            # if body in htp_request

            body_params = http_request.body.keys()

            if "specie_name" in body_params:
                name = http_request.body["specie_name"]
                response = self.register_specie_use_case.register_specie(specie_name=name)
                self.log.info(f"Registering Specie with Name: {name}")

            else:
                response = {"Success": False, "Data": None}
                self.log.warning("Invalid body parameters for registering Specie")

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                self.log.error("Error occurred while registering Specie")
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

            self.log.info("Specie registered successfully")
            return HttpResponse(status_code=200, body=response["Data"])

        # If no body in http_request
        http_error = HttpErrors.error_400()
        self.log.error("Bad Request: No body provided")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
