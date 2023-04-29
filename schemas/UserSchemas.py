from pydantic import BaseModel


class UserAuth(BaseModel):
    email: str | None
    password: str | None


class User(BaseModel):
    name: str
    age: int
    id: int

    class Config:
        orm_mode = True
