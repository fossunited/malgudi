#! /usr/bin/env python
"""
Script to run the malgudi webapp using development web server.

Usage:

    export FLASK_DEBUG=1
    python run.py

The database migrations are automatically run on startup. To run only the db
migrations, use:

    python run.py --migrate
"""
from webapp.app import app
from webapp.migrate import migrate

if __name__ == "__main__":
    if "--migrate" in sys.argv:
        migrate()
    else:
        migrate()
        app.run()
