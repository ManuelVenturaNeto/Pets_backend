from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Pets(Base):
    """
    Pets Entity
    """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specie = Column(Integer, ForeignKey("species.id"), nullable=False)
    age = Column(Integer)
    animal_shelter_id = Column(
        Integer, ForeignKey("animal_shelters.id"), nullable=False
    )
    adopted = Column(Boolean, default=False)
    user_adopters = relationship("UserAdopters")

    def __repr__(self):
        return f"Pet [name = {self.name}, specie = {self.specie}, animal_shelter_id = {self.animal_shelter_id}, adopted = {self.adopted}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.specie == other.specie
            and self.age == other.age
            and self.animal_shelter_id == other.animal_shelter_id
            and self.adopted == other.adopted
        ):
            return True
        return False
