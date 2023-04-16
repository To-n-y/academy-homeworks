from models.user import User

users_list = [
    User(1, "Ivan", "ivan@mail.ru", 18, "good boy", "123qwe"),
    User(2, "Pavel", "pavel@mail.ru", 19, "None", "12345678"),
    User(3, "Viktor", "viktor@mail.ru", 20, "N", "adlvwern234"),
    User(4, "qwe", "qwe", 12, "qwe", "$2b$12$pEVu0rLz9GFtJwCupRnoH.PzCkUM8GuGga1nNwF1O1wa9bj50MJ1.")
]
relations_dict = {2: [1], 1: [2]}
