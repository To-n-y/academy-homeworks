from dotenv import load_dotenv
from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
ALGORITHM = "HS256"


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret1")
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(
    subject: Union[str, Any], expires_delta: int | None = None
) -> str:
    if expires_delta is not None:
        expires_delta += datetime.utcnow()
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


# if __name__ == "__main__":
#    print(JWT_SECRET_KEY)
