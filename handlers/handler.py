from fastapi import APIRouter, HTTPException
from starlette import status

from models.user import User
from service.user import Service


class Handler(object):
    def __init__(self, service: Service, router: APIRouter):
        self._router = router
        self.service = service

    def home(self):
        return {"message": "OK"}

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
        self, id: int, name: str, email: str, age: int, about: str
    ):
        user = User(id, name, email, age, about)
        res = self.service.create_user(user)
        if res == 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User is already exist",
            )
        else:
            return user

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

    def edit_user(self, id: int, name: str, email: str, age: int, about: str):
        user = User(id=id, name=name, email=email, age=age, about=about)
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
        self._router.get("/users", status_code=status.HTTP_200_OK)(
            self.get_users
        )
        self._router.get("/user", status_code=status.HTTP_200_OK)(
            self.get_user
        )
        self._router.post("/user", status_code=status.HTTP_200_OK)(
            self.create_user
        )
        self._router.post(
            "/friends", response_model=dict, status_code=status.HTTP_200_OK
        )(self.create_friend)
        self._router.put("/user", status_code=status.HTTP_200_OK)(
            self.edit_user
        )
