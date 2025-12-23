import logging
from src.main.interfaces import RouteInterface
from src.presenters.controllers import RegisterUserAdopterController
from src.data.register_user_adopter import RegisterUserAdopter
from src.data.register_address import RegisterAddress
from src.data.find_pet import FindPet
from src.infra.repo.user_adopter_repository import UserAdopterRepository
from src.infra.repo.address_repository import AddressRepository
from src.infra.repo.pet_repository import PetRepository


def register_user_adopter_composer() -> RouteInterface:
    """
    Composing Register UserAdopter Route
    :param  - None
    :return - Object with Register UserAdopter Route
    """

    user_adopter_repository = UserAdopterRepository()
    address_repository = AddressRepository()
    address_service = RegisterAddress(address_repository)
    find_pet = FindPet(PetRepository())
    use_case = RegisterUserAdopter(user_adopter_repository, find_pet, address_service)
    register_user_adopter_route = RegisterUserAdopterController(use_case)

    return register_user_adopter_route
