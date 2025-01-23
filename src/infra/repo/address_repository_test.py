import pytest
from sqlalchemy import text
from faker import Faker
from src.infra.entities import Addresses as AddressesModel
from src.infra.config import DBConnectionHandler
from .address_repository import AddressRepository


faker = Faker("pt_BR")
address_repository = AddressRepository()
db_connection = DBConnectionHandler()


@pytest.mark.skip(reason="Sensive test")
def test_insert_address():
    """
    Should insert address in addresses table and return it
    """
    cep = str(faker.random_number(digits=8))
    state = faker.state_abbr()
    city = faker.city()
    neighborhood = faker.name()
    street = faker.name()
    complement = faker.street_name()
    number = faker.random_number(digits=2)

    new_address = address_repository.insert_address(
        cep=cep,
        state=state,
        city=city,
        neighborhood=neighborhood,
        street=street,
        complement=complement,
        number=number,
    )
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        query_address = connection.execute(
            text("SELECT * FROM addresses WHERE id=:id"), {"id": new_address.id}
        ).fetchone()

        connection.execute(
            text("DELETE FROM addresses WHERE id=:id"), {"id": new_address.id}
        )
        connection.commit()

    assert new_address.cep == query_address.cep
    assert new_address.state == query_address.state
    assert new_address.city == query_address.city
    assert new_address.neighborhood == query_address.neighborhood
    assert new_address.street == query_address.street
    assert new_address.complement == query_address.complement
    assert new_address.number == query_address.number


@pytest.mark.skip(reason="Sensive test")
def test_select_address():
    """
    Should select address in addresses table and return it
    """

    id = faker.random_number(digits=5)
    cep = str(faker.random_number(digits=8)).zfill(8)
    state = faker.state_abbr()
    city = faker.city()
    neighborhood = faker.name()
    street = faker.name()
    complement = faker.street_name()
    number = faker.random_number(digits=2)

    data = AddressesModel(
        id=id,
        cep=cep,
        state=state,
        city=city,
        neighborhood=neighborhood,
        street=street,
        complement=complement,
        number=number,
    )

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO addresses (id, cep, state, city, neighborhood, street, complement, number) \
                    VALUES (:id, :cep, :state, :city, :neighborhood, :street, :complement, :number)"
            ),
            {
                "id": id,
                "cep": cep,
                "state": state,
                "city": city,
                "neighborhood": neighborhood,
                "street": street,
                "complement": complement,
                "number": number,
            },
        )
        connection.commit()

        query_address1 = address_repository.select_address(address_id=data.id)
        query_address2 = address_repository.select_address(
            address_id=data.id, cep=data.cep
        )
        query_address3 = address_repository.select_address(cep=data.cep)
        query_address4 = address_repository.select_address(
            cep=data.cep,
            state=data.state,
            city=data.city,
            neighborhood=data.neighborhood,
            street=street,
            number=data.number,
        )

        connection.execute(text("DELETE FROM addresses WHERE id=:id"), {"id": data.id})
        connection.commit()

    assert data in query_address1
    assert data in query_address2
    assert data in query_address3
    assert data in query_address4


@pytest.mark.skip(reason="Sensive test")
def test_delete_address():
    """
    Should delete address in addresses table and return bool
    """
    id = faker.random_number(digits=5)
    cep = str(faker.random_number(digits=8)).zfill(8)
    state = faker.state_abbr()
    city = faker.city()
    neighborhood = faker.name()
    street = faker.name()
    complement = faker.street_name()
    number = faker.random_number(digits=2)

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO addresses (id, cep, state, city, neighborhood, street, complement, number) \
                    VALUES (:id, :cep, :state, :city, :neighborhood, :street, :complement, :number)"
            ),
            {
                "id": id,
                "cep": cep,
                "state": state,
                "city": city,
                "neighborhood": neighborhood,
                "street": street,
                "complement": complement,
                "number": number,
            },
        )
        connection.commit()

    deleted_element = address_repository.delete_address(id=id)

    assert deleted_element is True

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM addresses WHERE id = :id"), {"id": id}
        ).fetchone()
        assert result is None


@pytest.mark.skip(reason="Sensive test")
def test_update_address():
    """
    Should update address data in the addresses table and return the updated object
    """
    id = faker.random_number(digits=5)
    cep = str(faker.random_number(digits=8)).zfill(8)
    state = faker.state_abbr()
    city = faker.city()
    neighborhood = faker.name()
    street = faker.name()
    complement = faker.street_name()
    number = faker.random_number(digits=2)

    engine = db_connection.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(
                "INSERT INTO addresses (id, cep, state, city, neighborhood, street, complement, number) \
                    VALUES (:id, :cep, :state, :city, :neighborhood, :street, :complement, :number)"
            ),
            {
                "id": id,
                "cep": cep,
                "state": state,
                "city": city,
                "neighborhood": neighborhood,
                "street": street,
                "complement": complement,
                "number": number,
            },
        )
        connection.commit()

    new_city = faker.name()
    update_data = {
        "city": new_city,
        "complement": None,
    }

    updated_address = address_repository.update_address(id=id, **update_data)

    assert updated_address is not None
    assert updated_address.city == new_city
    assert not updated_address.complement
    assert updated_address.id == id

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT city, complement FROM addresses WHERE id = :id"), {"id": id}
        ).fetchone()

        connection.execute(text("DELETE FROM addresses WHERE id=:id"), {"id": id})
        connection.commit()

    assert result is not None
    assert result[0] == new_city
    assert not result[1]
