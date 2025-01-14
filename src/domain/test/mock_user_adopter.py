from faker import Faker
from src.domain.models import UserAdopter
from .mock_address import mock_address
from .mock_pets import mock_pets


faker = Faker()
address = mock_address()
pet = mock_pets()

def mock_user_adopters() -> UserAdopter:
    """
    Mocking UserAdopter
    """

    return UserAdopter(
        id=faker.random_number(digits=5),
        name=faker.name(),
        cpf=faker.random_number(digits=11),
        responsible_name=faker.name(),
        email=faker.email(),
        phone_number=faker.random_number(digits=11),
        address_id=address.id,
        pet_it= pet.id,
    )
