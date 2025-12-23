import logging
from typing import Dict
from src.domain.use_cases import RegisterSpecie as RegisterSpecieInterface
from src.data.interfaces import SpecieRepositoryInterface as SpecieRepository
from src.domain.models import Species


class RegisterSpecie(RegisterSpecieInterface):
    """
    Class to define usecase: Register Specie
    """

    def __init__(self, specie_repository: type[SpecieRepository]):
        self.specie_repository = specie_repository

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )


    def register_specie(self, specie_name: str) -> Dict[bool, Species]:
        """
        Register specie usecase
        :param  - specie_name: name of the specie
        :return - Disctionary with informations of the process
        """

        response = None

        validate_entry = isinstance(specie_name, str)
        self.log.info(f"Register Specie called with specie_name: {specie_name}")

        if validate_entry:
            response = self.specie_repository.insert_specie(specie_name=specie_name)
            self.log.info(f"Specie registered successfully: {response}")

        self.log.info(f"Register Specie called with specie_name: {specie_name}, Success: {validate_entry}")
        return {"Success": validate_entry, "Data": response}
