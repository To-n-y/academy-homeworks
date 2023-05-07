from fastapi import APIRouter

from app.handlers.user import UserHandler
from app.service.UserService import UserService

service = UserService()
routerUser = APIRouter()
routerUser.handler = UserHandler(service, routerUser)
routerUser.handler.add_route()
