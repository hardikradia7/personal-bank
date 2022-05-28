from fastapi import FastAPI
from app.utils import constants
from app.routes.v1 import ibans


def include_routes(cls: FastAPI, ver=None):
    if not ver:
        ver = "/" + constants.API + "/" + constants.VERSION_1

    cls.include_router(
        ibans.router,
        prefix=ver + "/" + constants.IBANS,
        tags=[constants.IBANS.capitalize()]
    )

