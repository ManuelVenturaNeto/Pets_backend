from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Addresses(Base):
    """
    Address Entity
    """

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    cep = Column(Integer, nullable=False)
    state = Column(String(2), nullable=False)
    city = Column(String, nullable=False)
    neighborhood = Column(String, nullable=False)
    street = Column(String, nullable=False)
    complement = Column(String)
    number = Column(Integer, nullable=False)
    address_id = relationship("UserAdopters")
    address_id = relationship("AnimalShelters")

    def __repr__(self):
        return f"Address [cep={self.cep}, state = {self.state}, city = {self.city}, neighborhood = {self.neighborhood}, street = {self.street}, complement = {self.complement}, number = {self.number}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.cep == other.cep
            and self.state == other.state
            and self.city == other.city
            and self.neighborhood == other.neighborhood
            and self.street == other.street
            and self.number == other.number
            and self.complement == other.complement
        ):
            return True
        return False
