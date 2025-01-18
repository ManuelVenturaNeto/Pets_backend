from faker import Faker
from src.domain.models import Addresses

faker = Faker("pt_BR")


def mock_address() -> Addresses:
    """
    Mocking Addresses
    """

    return Addresses(
        id=faker.random_number(digits=5),
        cep=str(faker.random_number(digits=8)).zfill(8),
        state=faker.state_abbr(),
        city=faker.name(),
        neighborhood=faker.name(),
        street=faker.name(),
        number=faker.random_number(digits=3),
        complement=faker.name(),
    )
