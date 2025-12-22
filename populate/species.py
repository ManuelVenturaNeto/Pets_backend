import logging
import sys
from pathlib import Path
from typing import Any, List

from sqlalchemy import exc, text
from sqlalchemy.engine import Connection
from src.infra.config.db_config import DBConnectionHandler

# Add the project root to sys.path
project_root: Path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def _execute_schema_sql(db_connection: Connection, schema_sql_file_path: Path) -> None:
    """
    Execute SQL statements from init/schema.sql to create tables if they do not exist.
    """
    if not schema_sql_file_path.exists():
        raise FileNotFoundError(f"schema.sql not found at: {schema_sql_file_path}")

    schema_sql_content: str = schema_sql_file_path.read_text(encoding="utf-8")

    # Naive split by ';' is usually enough for schema files (DDL).
    statement_list: List[str] = schema_sql_content.split(";")

    for statement in statement_list:
        cleaned_statement: str = statement.strip()
        if cleaned_statement == "":
            continue

        try:
            db_connection.execute(text(cleaned_statement))
        except exc.ProgrammingError as error:
            # If the schema.sql doesn't use IF NOT EXISTS, allow "already exists" to pass.
            error_message: str = str(getattr(error, "orig", error))
            if "already exists" in error_message.lower():
                logging.info("Objeto já existe, ignorando erro: %s", error_message)
                continue
            raise


def populate_species() -> None:
    """
    Populate the species table with predefined data
    """
    db_connection_handle: DBConnectionHandler = DBConnectionHandler()
    engine: Any = db_connection_handle.get_engine()

    species_list: List[str] = [
        "Dog",
        "Cat",
        "Rabbit",
        "Hamster",
        "Turtle",
        "Other",
    ]

    query: Any = text("INSERT INTO species (id, specie_name) VALUES (:id, :specie_name)")

    # Use Pets_backend/init/schema.sql (relative to this file)
    schema_sql_file_path: Path = Path(__file__).resolve().parent.parent / "init" / "schema.sql"

    try:
        with engine.connect() as db_connection:
            # Ensure schema exists before populating species
            _execute_schema_sql(db_connection, schema_sql_file_path)
            db_connection.commit()

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
