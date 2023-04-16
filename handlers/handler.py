from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from models.user import User
from service.user import Service
from utils import (
    get_hashed_password,
    verify_password,
    create_access_token,
)
from deps import get_current_user


class Handler(object):
    def __init__(self, service: Service, router: APIRouter):
        self._router = router
        self.service = service

    def home(self):
        return {"message": "OK"}

    def get_me(self, current_user: User = Depends(get_current_user)):
        return current_user

    def get_users(self):
        return self.service.get_users()

    def get_user(self, id: int):
        try:
            exist_user = self.service.get_user(id)
            return exist_user
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

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
        # TODO: username=login
        try:
            user = self.service.get_user_by_email(form_data.username)
        except Exception:
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

    def create_friend(self, first_id: int, second_id: int):
        res = self.service.add_relation(first_id, second_id)
        if res == 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found",
            )
        elif res == 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You can`t be friends with yourself",
            )
        elif res == 3:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You are already friends",
            )
        else:
            return {"message": "OK"}

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
        self._router.get(
            "/", response_model=dict, status_code=status.HTTP_200_OK
        )(self.home)
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
        self._router.post("/friends", status_code=status.HTTP_200_OK)(
            self.create_friend
        )
        self._router.put("/user", status_code=status.HTTP_200_OK)(
            self.edit_user
        )
