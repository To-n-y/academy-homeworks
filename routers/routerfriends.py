from fastapi import APIRouter

from handlers.friends import FriendsHandler
from service.user import Service

service = Service()
routerFriends = APIRouter()
routerFriends.handler = FriendsHandler(service, routerFriends)
routerFriends.handler.add_route()
