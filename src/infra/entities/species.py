from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.infra.config import Base


class Species(Base):
    """
    Species Entity
    """

    __tablename__ = "species"

    id = Column(Integer, primary_key=True, autoincrement=True)
    specie_name = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(TIMESTAMP(timezone=False), nullable=True)
    pets = relationship("Pets")



    def __repr__(self):
        return f"Specie [specie_name={self.specie_name}]"



    def __eq__(self, other):
        if self.id == other.id and self.specie_name == other.specie_name:
            return True
        return False
