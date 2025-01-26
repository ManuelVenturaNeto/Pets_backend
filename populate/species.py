# pylint: disable=W0718
import logging
import sys
from pathlib import Path
from sqlalchemy import text, exc
from src.infra.config.db_config import DBConnectionHandler

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


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

    try:
        with engine.connect() as db_connection:
            for index, specie in enumerate(species_list, start=1):
                db_connection.execute(query, {"id": index, "specie_name": specie})
            db_connection.commit()
            db_connection.execute(text("SELECT * FROM species ORDER BY id"))
            logging.info("Query executada com sucesso.")
    except exc.SQLAlchemyError:
        logging.error("Erro ao executar a query:", exc_info=True)
    except Exception:
        logging.error("Erro inesperado:", exc_info=True)


if __name__ == "__main__":
    populate_species()
