import os
import sqlite3
from abc import ABC

from app.config import DATABASE_URL
from app.service.ServiceInterface import ServiceInterface


class FriendService(ServiceInterface, ABC):
    # def __init__(self):

    def add_relation(self, first_id: int, second_id: int):
        db_path = os.path.join(os.getcwd(), 'db', DATABASE_URL)
        conn = sqlite3.connect(db_path)
        if first_id == second_id:
            return 2

        query1 = "SELECT * FROM User WHERE id = " + str(first_id) + ";"
        res1 = conn.execute(query1).fetchone()
        query2 = "SELECT * FROM User WHERE id = " + str(second_id) + ";"
        res2 = conn.execute(query2).fetchone()
        if res1 is None or res2 is None:
            return 1

        query3 = (
            "SELECT * FROM Friend WHERE first_id = "
            + str(first_id)
            + " AND second_id = "
            + str(second_id)
            + " ;"
        )
        res3 = conn.execute(query3).fetchone()
        if res3 is not None:
            return 3

        else:
            friend_data1 = (first_id, second_id)
            friend_data2 = (second_id, first_id)
            conn.execute(
                "INSERT INTO Friend(first_id, second_id) VALUES (?, ?)",
                friend_data1,
            )
            conn.execute(
                "INSERT INTO Friend(first_id, second_id) VALUES (?, ?)",
                friend_data2,
            )
            conn.commit()
        conn.close()
        return 4

    def is_friends(self, first_id: int, second_id: int):
        db_path = os.path.join(os.getcwd(), 'db', DATABASE_URL)
        conn = sqlite3.connect(db_path)
        if first_id == second_id:
            return 2

        query1 = "SELECT * FROM User WHERE id = " + str(first_id) + ";"
        res1 = conn.execute(query1).fetchone()
        query2 = "SELECT * FROM User WHERE id = " + str(second_id) + ";"
        res2 = conn.execute(query2).fetchone()
        if res1 is None or res2 is None:
            return 1

        query3 = (
            "SELECT * FROM Friend WHERE first_id = "
            + str(first_id)
            + " AND second_id = "
            + str(second_id)
            + " ;"
        )
        res3 = conn.execute(query3).fetchone()
        conn.close()
        if res3 is None:
            return 4
        else:
            return 3
