from src.data.find_specie import FindSpecie
from src.infra.repo.specie_repository import SpecieRepository
from src.presenters.controllers import FindSpecieController


def find_specie_composer() -> FindSpecieController:
    """
    Composing Find Specie Route
    :param  - None
    :return - Object with Find Specie Route
    """

    repository = SpecieRepository()
    use_case = FindSpecie(repository)
    find_specie_route = FindSpecieController(use_case)

    return find_specie_route
