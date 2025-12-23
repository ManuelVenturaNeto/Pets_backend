import datetime
import logging
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from sqlalchemy import exc, text
from sqlalchemy.engine import Connection
from src.infra.config.db_config import DBConnectionHandler

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def _execute_schema_sql(db_connection: Connection, schema_sql_file_path: Path) -> None:
    """
    Execute SQL statements from init/schema.sql to create tables if they do not exist.
    """
    if not schema_sql_file_path.exists():
        raise FileNotFoundError(f"schema.sql not found at: {schema_sql_file_path}")

    schema_sql_content = schema_sql_file_path.read_text(encoding="utf-8")

    statement_list = schema_sql_content.split(";")

    for statement in statement_list:
        cleaned_statement = statement.strip()
        if cleaned_statement == "":
            continue

        try:
            db_connection.execute(text(cleaned_statement))

        except exc.ProgrammingError as error:
            error_message = str(getattr(error, "orig", error))

            if "already exists" in error_message.lower():
                logging.debug("Objeto já existe, ignorando erro: %s", error_message)
                continue
            raise


def populate_species() -> None:
    """
    Populate the species table with predefined data
    """
    db_connection_handle = DBConnectionHandler()
    engine = db_connection_handle.get_engine()

    species_list = [
        "Dog",
        "Cat",
        "Rabbit",
        "Hamster",
        "Turtle",
        "Other",
    ]

    query = text(
        """
        INSERT INTO species (id, specie_name, created_at, updated_at, deleted_at)
        VALUES (:id, :specie_name, :created_at, :updated_at, :deleted_at)
        ON CONFLICT (id) DO NOTHING
        """
    )

    schema_sql_file_path = Path(__file__).resolve().parent.parent / "init" / "schema.sql"

    try:
        with engine.connect() as db_connection:
            _execute_schema_sql(db_connection, schema_sql_file_path)
            db_connection.commit()

            now_utc = datetime.datetime.now(datetime.timezone.utc)

            for index, specie in enumerate(species_list, start=1):
                db_connection.execute(
                    query,
                    {
                        "id": index,
                        "specie_name": specie,
                        "created_at": now_utc,
                        "updated_at": now_utc,
                        "deleted_at": None,
                    },
                )

            db_connection.commit()
            db_connection.execute(text("SELECT * FROM species ORDER BY id"))
            logging.debug("Query executada com sucesso.")

    except exc.SQLAlchemyError:
        logging.error("Erro ao executar a query:", exc_info=True)
    except Exception:
        logging.error("Erro inesperado:", exc_info=True)


if __name__ == "__main__":
    populate_species()
