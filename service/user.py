import abc

from models.user import User
from data.data import users_list, relations_dict


class ServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_users(self):
        pass

    def get_user(self, id: int):
        pass

    @abc.abstractmethod
    def create_user(self, user: User):
        pass

    @abc.abstractmethod
    def edit_user(self, id, user: User):
        pass

    @abc.abstractmethod
    def add_relation(self, first_id: int, second_id: int):
        pass


class Service(ServiceInterface):
    # def __init__(self):

    def get_users(self) -> list:
        return users_list

    def get_user(self, id: int) -> User:
        user = next((user for user in users_list if user.id == id), None)
        if user is None:
            raise Exception
        return user

    @classmethod
    def get_user_by_email(cls, email: str | None):
        if email is None:
            raise Exception
        user = next((user for user in users_list if user.email == email), None)
        if user is None:
            raise Exception
        return user

    def create_user(self, user: User) -> int:
        if user in users_list:
            return 1
        users_list.append(user)
        return 2

    def edit_user(self, id, user: User) -> int:
        exist_user = next((usr for usr in users_list if usr.id == id), None)
        if exist_user is None:
            return 1
        exist_user.name = user.name
        exist_user.email = user.email
        exist_user.age = user.age
        exist_user.about = user.about
        exist_user.password = user.password
        return 2

    def add_relation(self, first_id: int, second_id: int):
        first_user = next(
            (user for user in users_list if user.id == first_id), None
        )
        second_user = next(
            (user for user in users_list if user.id == second_id), None
        )
        if first_user is None or second_user is None:
            return 1
        if first_user == second_user:
            return 2
        tmp: list | None = relations_dict.get(first_id, None)
        if tmp is None:
            relations_dict[first_id] = []
            tmp = []
        if second_id in tmp:
            return 3
        tmp = relations_dict.get(second_id, None)
        if tmp is None:
            relations_dict[second_id] = []
        relations_dict[first_id].append(second_id)
        relations_dict[second_id].append(first_id)
        return 4

    def is_friends(self, first_id: int, second_id: int):
        first_user = next(
            (user for user in users_list if user.id == first_id), None
        )
        second_user = next(
            (user for user in users_list if user.id == second_id), None
        )
        if first_user is None or second_user is None:
            return 1
        if first_user == second_user:
            return 2
        tmp: list | None = relations_dict.get(first_id, None)
        if tmp is None:
            relations_dict[first_id] = []
            tmp = []
        if second_id in tmp:
            return 3
        else:
            return 4
