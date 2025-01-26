# pylint: disable=W0221

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

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Method to call use case
        """

        response = None

        if http_request.query:

            query_string_params = http_request.query.keys()

            if "user_adopter_id" in query_string_params:

                user_adopter_id = int(http_request.query["user_adopter_id"])

                response = self.find_user_adopter_use_case.by_user_adopter_id(
                    user_adopter_id=user_adopter_id
                )

            elif "pet_id" in query_string_params:

                pet_id = int(http_request.query["pet_id"])

                response = self.find_user_adopter_use_case.by_pet_id(pet_id=pet_id)

            elif any(
                key in query_string_params
                for key in ["name", "cpf", "email", "phone_number"]
            ):

                name = http_request.query.get("name", None)
                cpf = http_request.query.get("cpf", None)
                email = http_request.query.get("email", None)
                phone_number = http_request.query.get("phone_number", None)

                response = self.find_user_adopter_use_case.by_user_information(
                    name=name, cpf=cpf, email=email, phone_number=phone_number
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
