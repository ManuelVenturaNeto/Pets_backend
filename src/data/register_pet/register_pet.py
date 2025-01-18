# pylint: disable=W0237, R1701

from typing import Type, Dict, List
from src.domain.models import Pets, AnimalShelters, Species
from src.data.find_animal_shelter import FindAnimalShelter
from src.data.find_specie import FindSpecie
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository


class RegisterPet(RegisterPetInterface):
    """
    Class to define use case: Register Pet
    """

    def __init__(
        self,
        pet_repository: Type[PetRepository],
        find_animal_shelter: Type[FindAnimalShelter],
        find_specie: Type[FindSpecie],
    ):
        self.pet_repository = pet_repository
        self.find_animal_shelter = find_animal_shelter
        self.find_specie = find_specie

    def register_pet(
        self,
        name: str,
        specie_name: str,
        animal_shelter_information: Dict[int, str],
        adopted: bool,
        age: int = None,
    ) -> Dict[bool, Pets]:
        """
        :param: - name: pet name
                - specie_ name: name of specie
                - age: age of the pet
                - animal_shelter_information: Dictionary with animal_shelter_id and/or animal_shelter_name
                - adopted: status of pet adoption
        :return - Dictionary with information of the process
        """
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
            response = self.pet_repository.insert_pet(
                name=name,
                specie=specie["Data"][0].id,
                age=age,
                animal_shelter_id=animal_shelter["Data"][0].id,
                adopted=adopted,
            )

        return {"Success": checker, "Data": response}

    def __find_animal_shelter_information(
        self, animal_shelter_information: Dict[int, str]
    ) -> Dict[bool, List[AnimalShelters]]:
        """
        Check animal_shelter informations and select animal_shelter
        :param  - animal_shelter_information: Dictionary with animal_shelter_id and or animal_shelter_name
        :return - Dictionary with response of find_use case
        """

        animal_shelter_founded = None
        animal_shelter_params = animal_shelter_information.keys()

        if (
            "animal_shelter_id" in animal_shelter_params
            and "animal_shelter_name" in animal_shelter_params
        ):
            animal_shelter_founded = self.find_animal_shelter.by_id_and_name(
                animal_shelter_information["animal_shelter_id"],
                animal_shelter_information["animal_shelter_name"],
            )

        elif (
            "animal_shelter_id" not in animal_shelter_params
            and "animal_shelter_name" in animal_shelter_params
        ):
            animal_shelter_founded = self.find_animal_shelter.by_name(
                animal_shelter_information["animal_shelter_name"]
            )

        elif (
            "animal_shelter_id" in animal_shelter_params
            and "animal_shelter_name" not in animal_shelter_params
        ):
            animal_shelter_founded = self.find_animal_shelter.by_id(
                animal_shelter_information["animal_shelter_id"]
            )

        else:
            return {"Success": False, "Data": None}

        return animal_shelter_founded

    def __find_specie_information(self, specie_name: str) -> Dict[bool, List[Species]]:
        """
        Check animal_shelter informations and select animal_shelter
        :param  - specie_name: name of the specie
        :return - Dictionary with response of find_use case
        """

        specie_founded = None

        if specie_name:
            specie_founded = self.find_specie.by_specie_name(specie_name)

        else:
            return {"Success": False, "Data": None}

        return specie_founded
