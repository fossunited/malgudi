import web
from . import config

db = web.database(config.DATABASE_URL)

CURRENT_TIMESTAMP = web.sqlliteral("(current_timestamp at time zone 'utc')")

def get_sketch(id):
    return db.where("sketch", id=id).first()

def save_sketch(id, mode, title, code):
    db.update("sketch",
        mode=mode,
        title=title,
        code=code,
        last_updated=CURRENT_TIMESTAMP,
        where="id=$id",
        vars={"id": id})

def new_sketch(mode, title, code):
    """Creates a new sketch and returns the id.
    """
    return db.insert("sketch",
        mode=mode,
        title=title,
        code=code)
