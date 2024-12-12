from faker import Faker
from src.domain.models import Pets
from src.infra.entities.pets import AnimalTypes


faker = Faker()


def mock_pets() -> Pets:
    """
    Mocking Pets
    """

    return Pets(
        id=faker.random_number(digits=5),
        name=faker.name(),
        species=faker.enum(AnimalTypes),
        age=faker.random_number(digits=2),
        user_id=faker.random_number(digits=5),
    )
