from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_NAME
from app.config import DATABASE_PASSWORD
from app.models.db_models import Friend
from app.service.UserService import UserService


class FriendService(ABC):
    # def __init__(self):

    def add_relation(self, friends: Friend) -> int:
        # id1 == id2: '2', not found: '1', already exists: '3', 4
        exist_user1 = UserService.get_user(friends.first_id)
        exist_user2 = UserService.get_user(friends.second_id)
        if exist_user1 == 1 or exist_user2 == 1:
            return 1
        if friends.first_id == friends.second_id:
            return 2
        engine = create_engine(
            f'postgresql://postgres:{DATABASE_PASSWORD}'
            f'@localhost:5432/{DATABASE_NAME}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        exists_friends = (
            session.query(Friend)
            .filter(
                Friend.first_id == friends.first_id
                and Friend.second_id == friends.second_id
            )
            .first()
        )
        if exists_friends is None:
            session.add(friends)
            friends2 = Friend(
                first_id=friends.second_id, second_id=friends.first_id
            )
            session.add(friends2)
            session.commit()
            session.refresh(friends)
            session.close()
            return 4
        else:
            session.close()
            return 3

    def is_friends(self, friends: Friend) -> int:
        exist_user1 = UserService.get_user(friends.first_id)
        exist_user2 = UserService.get_user(friends.second_id)
        if exist_user1 == 1 or exist_user2 == 1:
            return 1
        if friends.first_id == friends.second_id:
            return 2
        engine = create_engine(
            f'postgresql://postgres:{DATABASE_PASSWORD}'
            f'@localhost:5432/{DATABASE_NAME}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        exists_friends = (
            session.query(Friend)
            .filter(
                Friend.first_id == friends.first_id
                and Friend.second_id == friends.second_id
            )
            .first()
        )
        session.close()
        if exists_friends is None:
            return 4
        else:
            return 3
