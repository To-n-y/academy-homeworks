from fastapi import FastAPI, APIRouter

from service.user import Service
from handlers.handler import Handler

app = FastAPI()
router = APIRouter()
service = Service()
router.handler = Handler(service, router)
router.handler.add_route()
app.include_router(router)
