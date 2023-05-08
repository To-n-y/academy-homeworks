from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_NAME
from app.config import DATABASE_PASSWORD
from app.models.db_models import User
from app.service.ServiceInterface import UserServiceInterface


class UserService(UserServiceInterface, ABC):
    # def __init__(self):

    def get_users(self):
        engine = create_engine(
            f'postgresql://postgres:{DATABASE_PASSWORD}'
            f'@localhost:5432/{DATABASE_NAME}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        users = session.query(User).all()
        session.close()
        return users

    @classmethod
    def get_user(cls, id: int) -> int | User:
        engine = create_engine(
            f'postgresql://postgres:{DATABASE_PASSWORD}'
            f'@localhost:5432/{DATABASE_NAME}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter(User.id == id).first()
        session.close()
        if user is None:
            return 1
        return user

    @classmethod
    def get_user_by_email(cls, email: str | None) -> int | User:
        if email is None:
            return 1
        engine = create_engine(
            f'postgresql://postgres:{DATABASE_PASSWORD}'
            f'@localhost:5432/{DATABASE_NAME}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter(User.email == email).first()
        session.close()
        if user is None:
            return 1
        return user

    def create_user(self, user: User) -> int:
        exist_user = self.get_user(user.id)
        if exist_user != 1:
            return 1
        engine = create_engine(
            f'postgresql://postgres:{DATABASE_PASSWORD}'
            f'@localhost:5432/{DATABASE_NAME}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return 2

    def edit_user(self, id, user: User) -> int:
        exist_user = self.get_user(user.id)
        if exist_user == 1:
            return 1
        engine = create_engine(
            f'postgresql://postgres:{DATABASE_PASSWORD}'
            f'@localhost:5432/{DATABASE_NAME}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        user_from_db = session.query(User).get(id)
        for key, value in user.__dict__.items():
            if not key.startswith('_'):
                setattr(user_from_db, key, value)
        session.commit()
        session.close()
        return 2
