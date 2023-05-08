import psycopg2
from sqlalchemy import create_engine

from app.config import DATABASE_NAME
from app.config import DATABASE_PASSWORD
from app.models.db_models import Base


def main():
    conn = psycopg2.connect(
        host="localhost", user="postgres", password=f"{DATABASE_PASSWORD}"
    )
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    try:
        cur.execute(f"CREATE DATABASE {DATABASE_NAME}")
    except psycopg2.errors.DuplicateDatabase:
        print('Already exists')
    cur.close()
    conn.close()
    engine = create_engine(
        f'postgresql://postgres:{DATABASE_PASSWORD}'
        f'@localhost:5432/{DATABASE_NAME}'
    )

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
