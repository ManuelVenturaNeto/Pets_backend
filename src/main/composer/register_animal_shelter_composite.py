from src.main.interfaces import RouteInterface
from src.presenters.controllers import RegisterAnimalShelterController
from src.data.register_animal_shelter import RegisterAnimalShelter
from src.data.register_address import RegisterAddress
from src.infra.repo.animal_shelter_repository import AnimalShelterRepository
from src.infra.repo.address_repository import AddressRepository



def register_animal_shelter_composer() -> RouteInterface:
    """
    Composing Register AnimalShelter Route
    :param  - None
    :return - Object with Register AnimalShelter Route
    """

    animal_shelter_repository = AnimalShelterRepository()
    address_repository = AddressRepository()
    address_service = RegisterAddress(address_repository)
    use_case = RegisterAnimalShelter(animal_shelter_repository, address_service)
    register_animal_shelter_route = RegisterAnimalShelterController(use_case)

    return register_animal_shelter_route
