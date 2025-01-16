from faker import Faker
from src.domain.models import UserAdopters
from .mock_address import mock_address
from .mock_pet import mock_pet


faker = Faker("pt_BR")
address = mock_address()
pet = mock_pet()


def mock_user_adopter() -> UserAdopters:
    """
    Mocking UserAdopter
    """

    return UserAdopters(
        id=faker.random_number(digits=5),
        name=faker.name(),
        cpf=faker.random_number(digits=11),
        email=faker.email(),
        phone_number=faker.random_number(digits=11),
        address_id=address.id,
        pet_id=pet.id,
    )
