from faker import Faker
from src.domain.models import Species

faker = Faker()


def mock_specie() -> Species:
    """
    Mocking Species
    """

    return Species(
        id=faker.random_number(digits=1),
        specie_name=faker.name(),
    )
