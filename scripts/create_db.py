import os
import sqlite3

parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

db_path = os.path.join(parent_dir, "mydatabase.db")
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
conn.commit()

conn.close()
