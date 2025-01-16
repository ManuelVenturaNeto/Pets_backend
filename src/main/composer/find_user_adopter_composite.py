from src.data.find_user_adopter import FindUserAdopter
from src.infra.repo.user_adopter_repository import UserAdopterRepository
from src.presenters.controllers import FindUserAdopterController


def find_user_adopter_composer() -> FindUserAdopterController:
    """
    Composing Find UserAdopter Route
    :param  - None
    :return - Object with Find UserAdopter Route
    """

    repository = UserAdopterRepository()
    use_case = FindUserAdopter(repository)
    find_user_adopter_route = FindUserAdopterController(use_case)

    return find_user_adopter_route
