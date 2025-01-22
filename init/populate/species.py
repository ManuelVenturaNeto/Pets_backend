import sys
from pathlib import Path
from sqlalchemy import text
from src.infra.config.db_config import DBConnectionHandler

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))


def populate_species():
    """
    Populate the species table with predefined data
    """
    db_connection_handle = DBConnectionHandler()
    engine = db_connection_handle.get_engine()

    species_list = [
        "Dog",
        "Cat",
        "Rabbit",
        "Turtle",
        "Fish",
        "Snake",
        "Spider",
        "Horse",
        "Hamster",
        "Other",
    ]
    query = text("INSERT INTO species (id, specie_name) VALUES (:id, :specie_name)")

    with engine.connect() as conn:
        for index, specie in enumerate(species_list, start=1):
            conn.execute(query, {"id": index, "specie_name": specie})
        conn.commit()


if __name__ == "__main__":
    populate_species()
