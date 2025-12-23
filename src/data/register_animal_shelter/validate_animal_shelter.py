import logging
import re
from validate_docbr import CPF
from src.data.find_animal_shelter import FindAnimalShelter
from src.infra.repo.animal_shelter_repository import AnimalShelterRepository

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)


def validator(
    name: str,
    password: str,
    cpf: str,
    responsible_name: str,
    email: str,
    phone_number: str,
) -> bool:
    """
    Function to validade AnimalShelter data
    """

    validate_entry = (
        isinstance(name, str)
        and isinstance(password, str)
        and isinstance(cpf, str)
        and isinstance(responsible_name, str)
        and isinstance(email, str)
        and isinstance(phone_number, str)
    )
    log.info(f"Validating AnimalShelter with name: {name}, cpf: {cpf}, phone_number: {phone_number}")

    valid_name = validator_name(name)

    valid_password = validator_password(password)

    valid_cpf = validator_cpf(cpf)

    valid_phone_number = validator_phone_number(phone_number)

    if (
        validate_entry
        and valid_name
        and valid_password
        and valid_cpf
        and valid_phone_number
    ):
        log.info("AnimalShelter validation successful.")
        return True

    log.warning("AnimalShelter validation failed.")
    return False


def validator_name(name: str) -> bool:
    """
    Check if that name is not use in database
    """

    validation = FindAnimalShelter(AnimalShelterRepository()).by_name(name=name)

    if not validation["Data"]:
        log.info(f"Name {name} is valid and not in use.")
        return True

    log.warning(f"Name {name} is already in use.")
    return False


def validator_password(password: str) -> bool:
    """
    Check if the password is strong
    """
    password = str(password)

    if re.search(
        r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$", password
    ):
        log.info("Password is strong.")
        return True

    log.warning("Password is not strong enough.")
    return False


def validator_cpf(cpf: str) -> bool:
    """
    Check if the cpf isnt in database and if that cpf is valid
    """
    validation = FindAnimalShelter(AnimalShelterRepository()).by_cpf(cpf=cpf)

    if not validation["Data"]:
        cpf_str = str(cpf).zfill(11)
        cpf_validator = CPF().validate(cpf_str)
        if cpf_validator:
            log.info(f"CPF {cpf} is valid and not in use.")
        return cpf_validator

    log.warning(f"CPF {cpf} is already in use.")
    return False


def validator_phone_number(phone_number: str) -> bool:
    """
    Check phone number countin 11 digits
    """
    phone_number = str(phone_number)

    if len(phone_number) == 11:
        log.info(f"Phone number {phone_number} is valid.")
        return True

    log.warning(f"Phone number {phone_number} is invalid.")
    return False
