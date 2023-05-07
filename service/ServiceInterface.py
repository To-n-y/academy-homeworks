import abc

from models.user import User


class ServiceInterface:
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
