from sqlalchemy import text
from src.infra.config import DBConnectionHandler


def reset_auto_increment(table_name: str) -> None:
    """
    Reset the AUTO_INCREMENT of a table to the next value
    """
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        # descover the next id
        result = connection.execute(text(f"SELECT MAX(id) FROM {table_name}"))
        max_id = result.scalar() or 0  # If the table is empty, the result will be None
        next_id = max_id + 1

        connection.execute(text(f"ALTER TABLE {table_name} AUTO_INCREMENT = {next_id}"))
