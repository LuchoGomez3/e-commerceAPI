from fastapi import APIRouter

from modules.user import routes as RouterUser


def get_global_router():
    router = APIRouter()

    router.include_router(RouterUser)
