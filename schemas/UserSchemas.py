from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str


class TokenPayload(BaseModel):
    sub: str | None = None
    exp: int | None = None


class UserAuth(BaseModel):
    email: str | None
    password: str | None


class UserOut(BaseModel):
    id: int
    email: str


class SystemUser(UserOut):
    password: str
