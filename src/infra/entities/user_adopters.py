from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from src.infra.config import Base


class UserAdopters(Base):
    """
    User_Adopter Entity
    """

    __tablename__ = "user_adopters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(TIMESTAMP(timezone=False), nullable=True)



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
