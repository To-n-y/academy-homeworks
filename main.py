from fastapi import FastAPI

from routers.routerfriends import routerFriends
from routers.routeruser import routerUser

app = FastAPI()

app.include_router(routerUser)
app.include_router(routerFriends)
