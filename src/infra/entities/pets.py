from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.infra.config import Base


class Pets(Base):
    """
    Pets Entity
    """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    specie = Column(Integer, ForeignKey("species.id"), nullable=False)
    age = Column(Integer)
    animal_shelter_id = Column(Integer, ForeignKey("animal_shelters.id"), nullable=False)
    adopted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(TIMESTAMP(timezone=False), nullable=True)
    user_adopters = relationship("UserAdopters")



    def __repr__(self):
        return f"Pet [name = {self.name}, specie = {self.specie}, animal_shelter_id = {self.animal_shelter_id}]"



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
