from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from deps import get_current_user
from schemas.UserSchemas import UserAuth
from service.FriendInterface import FriendService
from service.UserInterface import UserService


class FriendsHandler(object):
    def __init__(self, service: FriendService, router: APIRouter):
        self._router = router
        self.service = service

    def create_friend(
        self,
        second_id: int,
        current_user: UserAuth = Depends(get_current_user),
    ):
        user = UserService.get_user_by_email(current_user.email)
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

    def add_route(self):
        self._router.post("/friends", status_code=status.HTTP_200_OK)(
            self.create_friend
        )
        self._router.post("/is_friends", status_code=status.HTTP_200_OK)(
            self.is_friend
        )