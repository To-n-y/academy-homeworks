import os
import sqlite3
from abc import ABC

from config import DATABASE_URL
from models.user import User
from service.ServiceInterface import ServiceInterface


class UserService(ServiceInterface, ABC):
    # def __init__(self):

    def get_users(self):
        db_path = os.path.join(os.getcwd(), 'db', DATABASE_URL)
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM User"
        res = conn.execute(query).fetchall()
        conn.close()
        return res

    def get_user(self, id: int) -> int | User:
        db_path = os.path.join(os.getcwd(), 'db', DATABASE_URL)
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM User WHERE id = " + str(id) + ";"
        res = conn.execute(query).fetchone()
        if res is None:
            return 1
        conn.close()
        return res

    @classmethod
    def get_user_by_email(cls, email: str | None) -> User:
        if email is None:
            return 1
        db_path = os.path.join(os.getcwd(), 'db', DATABASE_URL)
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM User WHERE email = " + "'" + email + "';"
        res = conn.execute(query).fetchone()
        print("XYU", res)
        if res is None:
            return 1
        conn.close()
        ###
        print(res)
        usr = User(*res)
        print("USER ", usr.password)
        return usr

    def create_user(self, user: User) -> int:
        db_path = os.path.join(os.getcwd(), 'db', DATABASE_URL)
        conn = sqlite3.connect(db_path)
        user_data = (
            user.id,
            user.name,
            user.email,
            user.age,
            user.about,
            user.password,
        )
        res = conn.execute(
            "INSERT OR IGNORE INTO User(id, name, email, "
            "age, about, password) VALUES (?, ?, ?, ?, ?, ?)",
            user_data,
        )
        cnt = res.rowcount
        conn.commit()
        conn.close()
        if cnt == 0:
            return 1
        else:
            return 2

    def edit_user(self, id, user: User) -> int:
        new_date = (
            user.name,
            user.email,
            user.age,
            user.about,
            user.password,
            user.id,
            user.id,
        )
        db_path = os.path.join(os.getcwd(), 'db', DATABASE_URL)
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(
            "UPDATE User SET name = ?, email = ?, age = ?,"
            " about = ?, password = ? WHERE id = ? AND EXISTS(SELECT 1 "
            "FROM User WHERE id = ?)",
            new_date,
        ).fetchone()
        conn.commit()
        res = c.rowcount
        conn.close()
        if res > 0:
            return 2
        else:
            return 1
