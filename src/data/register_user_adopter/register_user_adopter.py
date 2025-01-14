from typing import Type, Dict, List
from src.domain.models import UserAdopters, Pets
from src.domain.use_cases import RegisterUserAdopter as RegisterUserAdopterInterface
from src.data.interfaces import UserAdopterRepositoryInterface as UserRepository
from src.data.find_pet import FindPet
from src.data.register_address import RegisterAddress




class RegisterUserAdopter(RegisterUserAdopterInterface):
    """
    Class to define use case: Register User Adopter
    """
    
    def __init__(self, user_adopter_repository: Type[UserRepository], find_pet: type[FindPet], register_address_service: type[RegisterAddress]):
        self.user_adopter_repository = user_adopter_repository
        self.find_pet = find_pet
        self.register_address_service = register_address_service

    def register_user_adopter(self, name: str, cpf: int, email: str, phone_number: int, pet_id: int, cep: int, state: str, city: str, neighborhood: str, street: str, number: int, complement: str = None) -> Dict[bool, UserAdopters]:
        """
        
        """
        
        response = None
        
        validate_entry = (
            isinstance(name, str),
            isinstance(cpf, int),
            isinstance(email, str),
            isinstance(phone_number, int),
            isinstance(pet_id, int),
        )
        
        find_pet = self.__find_by_pet_id(pet_id)
        
        if validate_entry and find_pet["Success"]:
            address_response = self.register_address_service.register_address(cep=cep, state=state, city=city, neighborhood=neighborhood, street=street, number=number, complement=complement)
            
            if address_response["Success"]:
                address_id = address_response["Data"].id
                response = self.user_adopter_repository.insert_user_adopter(name=name, cpf=cpf, email=email, phone_number=phone_number, address_id=address_id, pet_id=pet_id)
                
            else:
                validate_entry = False

        return {"Success": validate_entry, "Data": response}

    def __find_by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """
        Check pet informations and select pet
        :param  - pet_id: Id of pet
        :return - Dictionary with response of find_use case
        """

        pet_founded = None
        
        if isinstance(pet_id): pet_founded = self.find_pet.by_pet_id(pet_id)

        else: return {"Success": False, "Data": None}

        return pet_founded