from typing import Dict, List
from src.domain.models import AnimalShelters
from src.domain.test import mock_animal_shelter


class FindAnimalShelterSpy:
    """
    Class to define usecase: Select AnimalShelter
    """

    def __init__(self, animal_shelter_repository: any):
        self.animal_shelter_repository = animal_shelter_repository
        self.by_id_param = {}
        self.by_name_param = {}
        self.by_id_and_name_param = {}

    def by_id(self, animal_shelter_id: int) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by id
        """

        self.by_id_param["animal_shelter_id"] = animal_shelter_id
        response = None
        validate_entry = isinstance(animal_shelter_id, int)

        if validate_entry:
            response = [mock_animal_shelter()]

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by animal_shelter_id
        :param  - name: name from animal_shelter
        :return - Dictionary of informations of the process
        """

        self.by_name_param["name"] = name
        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_animal_shelter()]

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, animal_shelter_id: int, name: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by animal_shelter_id and name
        :param  - animal_shelter_id: id from animal_shelter
                - name: name from animal_shelter
        :return - Dictionary of informations of the process
        """

        self.by_id_and_name_param["animal_shelter_id"] = animal_shelter_id
        self.by_id_and_name_param["name"] = name
        response = None
        validate_entry = isinstance(animal_shelter_id, int) and isinstance(name, str)

        if validate_entry:
            response = [mock_animal_shelter()]

        return {"Success": validate_entry, "Data": response}
