from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from app.models.user import User
from app.schemas.UserSchemas import UserAuth
from app.service.UserService import UserService
from app.utils.jwtutils import (
    get_hashed_password,
    verify_password,
    create_access_token,
)
from app.deps import get_current_user


class UserHandler(object):
    def __init__(self, service: UserService, router: APIRouter):
        self._router = router
        self.service = service

    def home(self):
        return {"message": "OK"}

    def get_me(self, current_user: UserAuth = Depends(get_current_user)):
        return current_user

    def get_users(self):
        res = self.service.get_users()
        if res is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Users not found"
            )
        return self.service.get_users()

    def get_user(self, id: int):
        exist_user = self.service.get_user(id)
        print(exist_user)
        if exist_user == 1:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return exist_user

    def create_user(
        self,
        id: int,
        name: str,
        email: str,
        age: int,
        about: str,
        password: str,
    ):
        user = User(
            id=id,
            name=name,
            email=email,
            age=age,
            about=about,
            password=get_hashed_password(password),
        )
        res = self.service.create_user(user)
        if res == 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User is already exist",
            )
        else:
            return user

    def login_user(self, form_data: OAuth2PasswordRequestForm = Depends()):
        user = self.service.get_user_by_email(form_data.username)
        if user == 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect name or email",
            )
        hashed_pass = user.password
        if not verify_password(form_data.password, hashed_pass):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password",
            )
        return {"access_token": create_access_token(user.email)}

    def edit_user(
        self,
        id: int,
        name: str,
        email: str,
        age: int,
        about: str,
        password: str,
    ):
        user = User(
            id=id,
            name=name,
            email=email,
            age=age,
            about=about,
            password=get_hashed_password(password),
        )
        res = self.service.edit_user(id, user)
        if res == 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found",
            )
        else:
            return user

    def add_route(self):
        self._router.get("/", status_code=status.HTTP_200_OK)(self.home)
        self._router.get("/me", status_code=status.HTTP_200_OK)(self.get_me)
        self._router.get("/users", status_code=status.HTTP_200_OK)(
            self.get_users
        )
        self._router.get("/user", status_code=status.HTTP_200_OK)(
            self.get_user
        )
        self._router.post("/signup", status_code=status.HTTP_200_OK)(
            self.create_user
        )
        self._router.post("/login", status_code=status.HTTP_200_OK)(
            self.login_user
        )
        self._router.put("/user", status_code=status.HTTP_200_OK)(
            self.edit_user
        )
