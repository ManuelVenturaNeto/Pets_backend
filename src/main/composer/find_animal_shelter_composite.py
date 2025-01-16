from src.data.find_animal_shelter import FindAnimalShelter
from src.infra.repo.animal_shelter_repository import AnimalShelterRepository
from src.presenters.controllers import FindAnimalShelterController


def find_animal_shelter_composer() -> FindAnimalShelterController:
    """
    Composing Find AnimalShelter Route
    :param  - None
    :return - Object with Find AnimalShelter Route
    """

    repository = AnimalShelterRepository()
    use_case = FindAnimalShelter(repository)
    find_animal_shelter_route = FindAnimalShelterController(use_case)

    return find_animal_shelter_route
