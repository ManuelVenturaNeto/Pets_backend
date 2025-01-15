from faker import Faker
from src.domain.models import AnimalShelters
from .mock_address import mock_address


faker = Faker()
address = mock_address()

def mock_animal_shelter() -> AnimalShelters:
    """
    Mocking AnimalShelters
    """

    return AnimalShelters(
        id=faker.random_number(digits=5),
        name=faker.name(),
        password=faker.password(),
        cpf=faker.random_number(digits=11),
        responsible_name=faker.name(),
        email=faker.email(),
        phone_number=faker.random_number(digits=11),
        address_id=address.id,
    )
