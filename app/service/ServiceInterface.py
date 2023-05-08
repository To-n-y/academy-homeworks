import abc

from app.models.db_models import User


class UserServiceInterface:
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
