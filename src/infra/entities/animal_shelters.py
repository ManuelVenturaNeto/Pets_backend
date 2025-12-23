from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config import Base


class AnimalShelters(Base):
    """
    AnimalShelters Entity
    """

    __tablename__ = "animal_shelters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    responsible_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)
    id_pet = relationship("Pets")



    def __repr__(self):
        return f"AnimalShelter [name = {self.name}, password = {self.password}]"



    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.password == other.password
            and self.cpf == other.cpf
            and self.responsible_name == other.responsible_name
            and self.email == other.email
            and self.phone_number == other.phone_number
            and self.address_id == other.address_id
        ):
            return True
        return False
