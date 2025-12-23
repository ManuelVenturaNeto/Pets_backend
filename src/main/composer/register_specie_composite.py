import logging
from src.main.interfaces import RouteInterface
from src.presenters.controllers import RegisterSpecieController
from src.data.register_specie import RegisterSpecie
from src.infra.repo.specie_repository import SpecieRepository



def register_specie_composer() -> RouteInterface:
    """
    Composing Register Specie Route
    :param  - None
    :return - Object with Register Specie Route
    """

    specie_repository = SpecieRepository()
    use_case = RegisterSpecie(specie_repository)
    register_specie_route = RegisterSpecieController(use_case)

    return register_specie_route
