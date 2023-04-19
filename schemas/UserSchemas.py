from pydantic import BaseModel


class UserAuth(BaseModel):
    email: str | None
    password: str | None


class UserOut(BaseModel):
    id: int
    email: str


class SystemUser(UserOut):
    password: str
