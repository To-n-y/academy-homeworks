from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str | None = None
    exp: int | None = None


class UserAuth(BaseModel):
    email: str = Field(..., description="user email")
    password: str = Field(
        ..., min_length=5, max_length=24, description="user password"
    )


class UserOut(BaseModel):
    id: int
    email: str


class SystemUser(UserOut):
    password: str
