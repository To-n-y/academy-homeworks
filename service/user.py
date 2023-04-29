import abc
import os
import sqlite3
from sqlite3 import Cursor

from config import DATABASE_URL
from data.data import users_list, relations_dict
from models.Users import User


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

    def get_users(self):
        db_path = os.path.join(os.getcwd(), DATABASE_URL)
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM User"
        res = conn.execute(query).fetchall()
        conn.close()
        return res

    def get_user(self, id: int) -> int | User:
        db_path = os.path.join(os.getcwd(), DATABASE_URL)
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM User WHERE id = " + str(id) + ";"
        res = conn.execute(query).fetchone()
        if res is None:
            return 1
        conn.close()
        return res

    @classmethod
    def get_user_by_email(cls, email: str | None):
        if email is None:
            return 1
        db_path = os.path.join(os.getcwd(), DATABASE_URL)
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM User WHERE email = " + email + ";"
        res = conn.execute(query).fetchone()
        if res is None:
            return 1
        conn.close()
        return res

    def create_user(self, user: User) -> int:
        db_path = os.path.join(os.getcwd(), DATABASE_URL)
        conn = sqlite3.connect(db_path)
        user_data = (user.id, user.name, user.email, user.age, user.about, user.password)
        res = conn.execute(
            "INSERT OR IGNORE INTO User(id, name, email, age, about, password) VALUES (?, ?, ?, ?, ?, ?)",
            user_data)
        if res.rowcount == 0:
            return 1
        conn.commit()
        conn.close()
        return 2

    def edit_user(self, id, user: User) -> int:
        new_date = (user.name, user.email, user.age, user.about, user.password, user.id, user.id)
        exist_user = next((usr for usr in users_list if usr.id == id), None)
        db_path = os.path.join(os.getcwd(), DATABASE_URL)
        conn = sqlite3.connect(db_path)
        user_data = (user.id, user.name, user.email, user.age, user.about, user.password)
        c = conn.cursor()
        c.execute("UPDATE User SET name = ?, email = ?, age = ?, about = ?, password = ?"
                  " WHERE id = ? AND EXISTS(SELECT 1 FROM User WHERE id = ?)", new_date).fetchone()
        conn.commit()
        res = c.rowcount
        conn.close()
        if res > 0:
            return 2
        else:
            return 1

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
