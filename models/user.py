class User:
    id: int
    name: str
    email: str
    age: int
    about: str

    def __init__(self, id, name, email, age, about):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.about = about

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, " \
               f"email={self.email}, age={self.age}, about={self.about})"

    def __eq__(self, other):
        return self.id == other.id

    def json(self):
        return {"id": self.id, "name": self.name,
                "email": self.email, "age": self.age, "about": self.about}
