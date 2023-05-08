import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret")
DATABASE_NAME = os.getenv("DATABASE_NAME", "name")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
