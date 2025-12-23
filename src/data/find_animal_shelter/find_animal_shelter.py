import logging
from typing import Type, Dict, List
from src.domain.models import AnimalShelters
from src.domain.use_cases import FindAnimalShelter as FindAnimalShelterInterface
from src.data.interfaces import AnimalShelterRepositoryInterface as AnimalShelterRepository


class FindAnimalShelter(FindAnimalShelterInterface):
    """
    Class to define use case Find AnimalShelter
    """

    def __init__(self, animal_shelter_repository: Type[AnimalShelterRepository]):

        self.animal_shelter_repository = animal_shelter_repository

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )


    def by_id(self, id: int) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by id
        :param  - id: id from animal_shelter
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(id, int)
        self.log.info(f"Find AnimalShelter by id called with id: {id}")

        if validate_entry:
            response = self.animal_shelter_repository.select_animal_shelter(id=id)
            self.log.info(f"AnimalShelter found for id {id}: {response}")

        self.log.info(f"Find AnimalShelter by id called with id: {id}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}



    def by_name(self, name: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by id
        :param  - name: name from animal_shelter
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)
        self.log.info(f"Find AnimalShelter by name called with name: {name}")

        if validate_entry:
            response = self.animal_shelter_repository.select_animal_shelter(name=name)
            self.log.info(f"AnimalShelter found for name {name}: {response}")

        self.log.info(f"Find AnimalShelter by name called with name: {name}, Success: {validate_entry}")
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
        self.log.info(f"Find AnimalShelter by id and name called with id: {id}, name: {name}")

        if validate_entry:
            response = self.animal_shelter_repository.select_animal_shelter(id=id, name=name)
            self.log.info(f"AnimalShelter found for id {id} and name {name}: {response}")

        self.log.info(f"Find AnimalShelter by id and name called with id: {id}, name: {name}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}



    def by_cpf(self, cpf: str) -> Dict[bool, List[AnimalShelters]]:
        """
        Select AnimalShelter by id
        :param  - cpf: cpf from animal_shelter
        :return - Dictionary of informations of the process
        """

        response = None
        validate_entry = isinstance(cpf, int)
        self.log.info(f"Find AnimalShelter by cpf called with cpf: {cpf}")

        if validate_entry:
            response = self.animal_shelter_repository.select_animal_shelter(cpf=cpf)
            self.log.info(f"AnimalShelter found for cpf {cpf}: {response}")

        self.log.info(f"Find AnimalShelter by cpf called with cpf: {cpf}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}
