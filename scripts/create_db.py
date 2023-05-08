import psycopg2
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.config import DATABASE_NAME
from app.config import DATABASE_PASSWORD


def main():
    conn = psycopg2.connect(host="localhost", user="postgres", password=f"{DATABASE_PASSWORD}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE {DATABASE_NAME}")
    cur.close()
    conn.close()
    engine = create_engine(f'postgresql://postgres:{DATABASE_PASSWORD}@localhost:5432/{DATABASE_NAME}')

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'Users'
        id = Column(Integer, primary_key=True)
        name = Column(String(50), nullable=False)
        email = Column(String(50), nullable=False)
        age = Column(Integer)
        about = Column(String(50), nullable=False)
        password = Column(String(50), nullable=False)

    class Friend(Base):
        __tablename__ = 'Friends'
        id = Column(Integer, primary_key=True)
        first_id = Column(Integer)
        second_id = Column(Integer)

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
