from fastapi import FastAPI
from app.utils import consts
from app.routes.v1 import iban


def include_routes(cls: FastAPI, ver=None):
    if not ver:
        ver = "/" + consts.API + "/" + consts.VERSION_1

    cls.include_router(
        iban.router,
        prefix=ver + "/" + consts.IBAN,
        tags=[consts.IBAN.capitalize()]
    )

