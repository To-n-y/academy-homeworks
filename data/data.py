from models.user import User

users_list = [
    User(1, "Ivan", "ivan@mail.ru", 18, "good boy", "123qwe"),
    User(2, "Pavel", "pavel@mail.ru", 19, "None", "12345678"),
    User(3, "Viktor", "viktor@mail.ru", 20, "N", "adlvwern234"),
    User(4, "qwe", "qwe", 12, "qwe", "qwe")
]
relations_dict = {2: [1], 1: [2]}
