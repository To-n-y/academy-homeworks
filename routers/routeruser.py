from fastapi import APIRouter

from handlers.user import UserHandler
from service.user import Service

service = Service()
routerUser = APIRouter()
routerUser.handler = UserHandler(service, routerUser)
routerUser.handler.add_route()
