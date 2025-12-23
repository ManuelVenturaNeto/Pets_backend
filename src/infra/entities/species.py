from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Species(Base):
    """
    Species Entity
    """

    __tablename__ = "species"

    id = Column(Integer, primary_key=True, autoincrement=True)
    specie_name = Column(String, unique=True, nullable=False)
    pets = relationship("Pets")



    def __repr__(self):
        return f"Specie [specie_name={self.specie_name}]"



    def __eq__(self, other):
        if self.id == other.id and self.specie_name == other.specie_name:
            return True
        return False
