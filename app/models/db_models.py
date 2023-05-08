from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    age = Column(Integer)
    about = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)


class Friend(Base):
    __tablename__ = 'Friends'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_id = Column(Integer)
    second_id = Column(Integer)
