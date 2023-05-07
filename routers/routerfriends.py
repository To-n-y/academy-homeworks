from fastapi import APIRouter

from handlers.friends import FriendsHandler
from service.FriendInterface import FriendService

service = FriendService()
routerFriends = APIRouter()
routerFriends.handler = FriendsHandler(service, routerFriends)
routerFriends.handler.add_route()
