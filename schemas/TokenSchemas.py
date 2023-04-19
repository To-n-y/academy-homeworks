from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str


class TokenPayload(BaseModel):
    sub: str | None = None
    exp: int | None = None
