import logging
from typing import Type
from src.main.interfaces import RouteInterface
from src.domain.use_cases import FindUserAdopter
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindUserAdopterController(RouteInterface):
    """
    Class to define controller to find_user_adopter use case
    """

    def __init__(self, find_user_adopter_use_case: Type[FindUserAdopter]):
        self.find_user_adopter_use_case = find_user_adopter_use_case

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

            if "user_adopter_id" in query_string_params:

                user_adopter_id = int(http_request.query_params["user_adopter_id"])
                response = self.find_user_adopter_use_case.by_user_adopter_id(user_adopter_id=user_adopter_id)
                self.log.info(f"Finding User Adopter by ID: {user_adopter_id}")

            elif "pet_id" in query_string_params:

                pet_id = int(http_request.query_params["pet_id"])
                response = self.find_user_adopter_use_case.by_pet_id(pet_id=pet_id)
                self.log.info(f"Finding User Adopter by Pet ID: {pet_id}")

            elif any(key in query_string_params for key in ["name", "cpf", "email", "phone_number"]):

                name = http_request.query_params.get("name", None)
                cpf = http_request.query_params.get("cpf", None)
                email = http_request.query_params.get("email", None)
                phone_number = http_request.query_params.get("phone_number", None)
                
                response = self.find_user_adopter_use_case.by_user_information(name=name, cpf=cpf, email=email, phone_number=phone_number)
                self.log.info("Finding User Adopter by provided user information")

            else:
                response = {"Success": False, "Data": None}
                self.log.warning("Invalid query parameters for finding User Adopter")

            if response["Success"] is False:

                http_error = HttpErrors.error_422()
                self.log.error("Error occurred while finding User Adopter")
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

            self.log.info("User Adopter found successfully")
            return HttpResponse(status_code=200, body=response["Data"])

        # if no query in http_request
        http_error = HttpErrors.error_400()
        self.log.error("Bad Request: No query parameters provided")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
