from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from models.user import User
from schemas.UserSchemas import UserAuth
from service.user import Service
from utils.jwtutils import (
    get_hashed_password,
)
from deps import get_current_user


class FriendsHandler(object):
    def __init__(self, service: Service, router: APIRouter):
        self._router = router
        self.service = service

    def create_friend(
        self,
        second_id: int,
        current_user: UserAuth = Depends(get_current_user),
    ):
        user = Service.get_user_by_email(current_user.email)
        res = self.service.add_relation(user.id, second_id)
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

    def is_friend(self, first_id: int, second_id: int):
        res = self.service.is_friends(first_id, second_id)
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
            return {"message": "Yes"}
        else:
            return {"message": "No"}

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
        self._router.post("/friends", status_code=status.HTTP_200_OK)(
            self.create_friend
        )
        self._router.post("/is_friends", status_code=status.HTTP_200_OK)(
            self.is_friend
        )
