import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """
    Define Animal Types
    """

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
    TURTLE = "turtle"
    RABBIT = "rabbit"
    MOUSE = "mouse"
    HAMSTER = "hamster"
    PARROT = "parrot"


class Pets(Base):
    """
    Pets Entity
    """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    species = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return (
            f"Pet [name={self.name}, specie = {self.species}, user_id = {self.user_id}]"
        )

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.species == other.species
            and self.age == other.age
            and self.user_id == other.user_id
        ):
            return True
        return False
