import logging
from typing import Type
from src.main.interfaces import RouteInterface
from src.domain.use_cases import RegisterPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterPetController(RouteInterface):
    """
    Class to Define route to register_pet use case
    """

    def __init__(self, register_pet_use_case: Type[RegisterPet]):
        self.register_pet_use_case = register_pet_use_case

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

            if "name" in body_params and "specie_name" in body_params and "animal_shelter_information" in body_params:
                # if body param contain correct items
                self.log.info("Registering Pet with provided information")

                animal_shelter_information_params = http_request.body["animal_shelter_information"].keys()
                if "animal_shelter_id" in animal_shelter_information_params or "animal_shelter_name" in animal_shelter_information_params:
                    # if animal_shelter_information contain correct items

                    name = http_request.body["name"]
                    specie_name = http_request.body["specie_name"]
                    animal_shelter_information = http_request.body["animal_shelter_information"]
                    self.log.debug(f"Animal Shelter Information: {animal_shelter_information}")

                    if "age" in body_params:
                        age = http_request.body["age"]

                    else:
                        age = None

                    adopted = False

                    response = self.register_pet_use_case.register_pet(
                        name=name,
                        specie_name=specie_name,
                        animal_shelter_information=animal_shelter_information,
                        age=age,
                        adopted=adopted,
                    )
                    self.log.info("Pet registered successfully")

                else:
                    response = {"Success": False, "Data": None}
                    self.log.warning("Invalid animal_shelter_information parameters for registering Pet")

            else:
                response = {"Success": False, "Data": None}
                self.log.warning("Invalid body parameters for registering Pet")

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                self.log.error("Error occurred while registering Pet")
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

            self.log.info("Pet registered successfully")
            return HttpResponse(status_code=200, body=response["Data"])

        # If no body in http_request
        http_error = HttpErrors.error_400()
        self.log.error("Bad Request: No body provided")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
