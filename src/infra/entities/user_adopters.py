from sqlalchemy import Column, String, Integer, ForeignKey
from src.infra.config import Base


class UserAdopters(Base):
    """
    User_Adopter Entity
    """

    __tablename__ = "user_adopters"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    cpf = Column(Integer, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(Integer, unique=True, nullable=False)
    address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)


    def __repr__(self):
        return f"User_Adopter [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.cpf == other.cpf
            and self.email == other.email
            and self.phone_number == other.phone_number
            and self.address_id == other.address_id
            and self.pet_id == other.pet_id
        ):
            return True
        return False
