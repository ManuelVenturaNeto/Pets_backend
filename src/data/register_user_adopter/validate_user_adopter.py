import logging
from validate_docbr import CPF


log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)


def validator(name: str, cpf: str, email: str, phone_number: str, pet_id: int) -> bool:
    """
    Function to validade UserAdopter data
    """

    validate_entry = (
        isinstance(name, str)
        and isinstance(cpf, str)
        and isinstance(email, str)
        and isinstance(phone_number, str)
        and isinstance(pet_id, int)
    )

    valid_cpf = validator_cpf(cpf)

    valid_phone_number = validator_phone_number(phone_number)

    if validate_entry and valid_cpf and valid_phone_number:
        log.info("UserAdopter validation successful.")
        return True

    log.warning("UserAdopter validation failed.")
    return False



def validator_cpf(cpf: str) -> bool:
    """
    Check if that cpf is valid
    """

    cpf_str = str(cpf).zfill(11)
    cpf_validator = CPF().validate(cpf_str)
    if cpf_validator:
        log.info(f"CPF {cpf} is valid.")

    log.warning(f"CPF {cpf} is invalid.")
    return cpf_validator



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
