from models.user import User

users_list = [
    User(1, "Ivan", "ivan@mail.ru", 18, "good boy"),
    User(2, "Pavel", "pavel@mail.ru", 19, "None"),
    User(3, "Viktor", "viktor@mail.ru", 20, "N"),
]
relations_dict = {2: [1], 1: [2]}
