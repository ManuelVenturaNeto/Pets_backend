import logging
from typing import Type
from src.main.interfaces import RouteInterface
from src.domain.use_cases import FindPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindPetController(RouteInterface):
    """
    Class to define find pet controller
    """

    def __init__(self, find_pet_use_case: Type[FindPet]):
        self.find_pet_use_case = find_pet_use_case

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

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "pet_id" in query_string_params and "animal_shelter_id" in query_string_params:
                pet_id = http_request.query["pet_id"]

                animal_shelter_id = http_request.query["animal_shelter_id"]
                response = self.find_pet_use_case.by_pet_id_and_animal_shelter_id(
                    pet_id=pet_id, animal_shelter_id=animal_shelter_id
                )
                self.log.info(f"Finding Pet by ID: {pet_id} and Animal Shelter ID: {animal_shelter_id}")

            elif (
                "pet_id" in query_string_params and "animal_shelter_id" not in query_string_params
            ):
                pet_id = http_request.query["pet_id"]
                response = self.find_pet_use_case.by_pet_id(pet_id=pet_id)
                self.log.info(f"Finding Pet by ID: {pet_id}")

            elif (
                "pet_id" not in query_string_params and "animal_shelter_id" in query_string_params
            ):
                animal_shelter_id = http_request.query["animal_shelter_id"]
                response = self.find_pet_use_case.by_animal_shelter_id(animal_shelter_id=animal_shelter_id)
                self.log.info(f"Finding Pet by Animal Shelter ID: {animal_shelter_id}")

            else:
                response = {"Success": False, "Data": None}
                self.log.warning("Invalid query parameters for finding Pet")

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                self.log.error("Error occurred while finding Pet")
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

            self.log.info("Pet found successfully")
            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        self.log.error("Bad Request: No query parameters provided")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
