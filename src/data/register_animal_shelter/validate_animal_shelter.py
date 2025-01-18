import re
from validate_docbr import CPF
from src.data.find_animal_shelter import FindAnimalShelter
from src.infra.repo.animal_shelter_repository import AnimalShelterRepository


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
        return True

    return False


def validator_name(name: str) -> bool:
    """
    Check if that name is not use in database
    """

    validation = FindAnimalShelter(AnimalShelterRepository()).by_name(name=name)

    if not validation["Data"]:
        return True

    return False


def validator_password(password: str) -> bool:
    """
    Check if the password is strong
    """
    password = str(password)

    if re.search(
        r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$", password
    ):
        return True

    return False


def validator_cpf(cpf: str) -> bool:
    """
    Check if the cpf isnt in database and if that cpf is valid
    """
    validation = FindAnimalShelter(AnimalShelterRepository()).by_cpf(cpf=cpf)

    if not validation["Data"]:
        cpf_str = str(cpf).zfill(11)
        cpf_validator = CPF().validate(cpf_str)

        return cpf_validator

    return False


def validator_phone_number(phone_number: str) -> bool:
    """
    Check phone number countin 11 digits
    """
    phone_number = str(phone_number)

    if len(phone_number) == 11:
        return True

    return False
