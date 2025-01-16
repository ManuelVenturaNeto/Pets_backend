# pylint: disable=W0237, R1701, W0231

from typing import Dict, List
from src.domain.test import mock_pet, mock_animal_shelter
from src.domain.models import Pets, AnimalShelters, Species
from src.data.test import FindSpecieSpy


class RegisterPetSpy(FindSpecieSpy):
    """
    Class to difine use case register pet
    """

    def __init__(self, pet_repository: any, find_animal_shelter: any, find_specie: any):
        self.pet_repository = pet_repository
        self.find_animal_shelter = find_animal_shelter
        self.find_specie = find_specie
        self.register_pet_param = {}

    def register_pet(
        self,
        name: str,
        specie_name: str,
        animal_shelter_information: Dict[int, str],
        adopted: bool,
        age: int = None,
    ) -> Dict[bool, Pets]:
        """
        Register pet
        """

        self.register_pet_param["name"] = name
        self.register_pet_param["specie_name"] = specie_name
        self.register_pet_param["animal_shelter_information"] = (
            animal_shelter_information
        )
        self.register_pet_param["age"] = age
        self.register_pet_param["adopted"] = adopted

        response = None

        validate_entry = isinstance(name, str) and (
            isinstance(age, int) or isinstance(age, type(None))
        )

        animal_shelter = self.__find_animal_shelter_information(
            animal_shelter_information
        )
        specie = self.__find_specie_information(specie_name)

        checker = validate_entry and animal_shelter["Success"] and specie["Success"]

        if checker:
            response = mock_pet()

        return {"Success": checker, "Data": response}

    def __find_animal_shelter_information(
        self, animal_shelter_information: Dict[int, str]
    ) -> Dict[bool, List[AnimalShelters]]:
        """
        Check animal_shelter informations
        """

        animal_shelter_founded = None
        animal_shelter_params = animal_shelter_information.keys()

        if (
            "animal_shelter_id" in animal_shelter_params
            and "animal_shelter_name" in animal_shelter_params
        ):
            animal_shelter_founded = {"Success": True, "Data": mock_animal_shelter()}

        elif (
            "animal_shelter_id" not in animal_shelter_params
            and "animal_shelter_name" in animal_shelter_params
        ):
            animal_shelter_founded = {"Success": True, "Data": mock_animal_shelter()}

        elif (
            "animal_shelter_id" in animal_shelter_params
            and "animal_shelter_name" not in animal_shelter_params
        ):
            animal_shelter_founded = {"Success": True, "Data": mock_animal_shelter()}

        else:
            return {"Success": False, "Data": None}

        return animal_shelter_founded

    def __find_specie_information(self, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Check animal_shelter informations
        """

        repo_specie_spy = FindSpecieSpy(self)

        specie_founded = None

        if specie_name:
            specie_founded = {
                "Success": True,
                "Data": repo_specie_spy.by_specie_name(specie_name),
            }

        else:
            return {"Success": False, "Data": None}

        return specie_founded
