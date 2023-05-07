import os
import sqlite3

from config import DATABASE_URL


def create_database():
    # parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'db'))
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    db_path = os.path.join(parent_dir, DATABASE_URL)

    conn = sqlite3.connect(db_path)

    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        age INTEGER,
        about TEXT,
        password TEXT
    );
    """
    )
    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS Friend (
        first_id INTEGER,
        second_id INTEGER
    );
    """
    )
    conn.commit()

    conn.close()


if __name__ == "__main__":
    create_database()
