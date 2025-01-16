from src.infra.repo.pet_repository import PetRepository
from src.infra.repo.animal_shelter_repository import AnimalShelterRepository
from src.infra.repo.specie_repository import SpecieRepository
from src.data.register_pet import RegisterPet
from src.data.find_animal_shelter import FindAnimalShelter
from src.data.find_specie import FindSpecie
from src.presenters.controllers import RegisterPetController


def register_pet_composer() -> RegisterPetController:
    """
    Composing Register Pet Route
    :param  - None
    :return - Object with Register pet Route
    """

    repository = PetRepository()
    find_animal_shelter_use_case = FindAnimalShelter(AnimalShelterRepository())
    find_specie_use_case = FindSpecie(SpecieRepository())
    use_case = RegisterPet(repository, find_animal_shelter_use_case, find_specie_use_case)
    register_pet_route = RegisterPetController(use_case)

    return register_pet_route
