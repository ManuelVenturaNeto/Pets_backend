# pylint: disable=arguments-differ

from typing import Type, Dict, List
from src.domain.models import AnimalShelters
from src.domain.use_cases import FindAnimalShelter as FindAnimalShelterInterface
from src.data.interfaces import (
    AnimalShelterRepositoryInterface as AnimalShelterRepository,
)


class FindAnimalShelter(FindAnimalShelterInterface):
    """
    Class to define use case Find AnimalShelter
    """

    def __init__(self, animal_shelter_repository: Type[AnimalShelterRepository]):

        self.animal_shelter_repository = animal_shelter_repository

    def by_id(self, id: int) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by id
        :param  - id: id from animal_shelter
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = self.animal_shelter_repository.select_animal_shelter(id=id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by id
        :param  - name: name from animal_shelter
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.animal_shelter_repository.select_animal_shelter(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, id: int, name: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by id and name
        :param  - id: id from animal_shelter
                - name: name from animal_shelter
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(id, int) and isinstance(name, str)

        if validate_entry:
            response = self.animal_shelter_repository.select_animal_shelter(
                id=id, name=name
            )

        return {"Success": validate_entry, "Data": response}

    def by_cpf(self, cpf: int) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by id
        :param  - cpf: cpf from animal_shelter
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(cpf, int)

        if validate_entry:
            response = self.animal_shelter_repository.select_animal_shelter(cpf=cpf)

        return {"Success": validate_entry, "Data": response}
