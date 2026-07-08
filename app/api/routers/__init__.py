from fastapi import FastAPI

from . import users, auth


def include_routers(app: FastAPI):
    app.include_router(users.router)
    app.include_router(auth.router)
