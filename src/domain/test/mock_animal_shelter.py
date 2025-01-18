from faker import Faker
from src.domain.models import AnimalShelters
from .mock_address import mock_address


faker = Faker("pt_BR")
address = mock_address()


def mock_animal_shelter() -> AnimalShelters:
    """
    Mocking AnimalShelters
    """

    return AnimalShelters(
        id=faker.random_number(digits=5),
        name=faker.name(),
        password=faker.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
        cpf=faker.cpf().replace(".", "").replace("-", ""),
        responsible_name=faker.name(),
        email=faker.email(),
        phone_number=str(faker.random_number(digits=11)).zfill(11),
        address_id=address.id,
    )
