from fastapi import APIRouter

from handlers.user import UserHandler
from service.UserInterface import UserService

service = UserService()
routerUser = APIRouter()
routerUser.handler = UserHandler(service, routerUser)
routerUser.handler.add_route()
