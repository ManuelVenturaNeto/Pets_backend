from faker import Faker
from src.domain.models import Pets


faker = Faker("pt_BR")


def mock_pet() -> Pets:
    """
    Mocking Pets
    """

    return Pets(
        id=faker.random_number(digits=5),
        name=faker.name(),
        species=faker.random_number(digits=1),
        age=faker.random_number(digits=2),
        animal_shelter_id=faker.random_number(digits=5),
        adopted=faker.boolean(),
    )
