from pathlib import Path
import web
from . import config
from niftyhacks.db import Schema

db = web.database(config.DATABASE_URL)
schema = Schema(db)

def migrate():
    """Migrates the database to latest schema.
    """
    init_schema()

def init_schema():
    if schema.has_table("sketch"):
        return

    sql = Path(__file__).parent.joinpath("schema.sql").read_text()
    db.query(sql)

if __name__ == "__main__":
    migrate()