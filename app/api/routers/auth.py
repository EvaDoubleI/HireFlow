from fastapi import APIRouter

from app import schemas

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/registrate", response_model=schemas.UserResponse)
def registrate_user(data: schemas.UserRegistrate):
    return {"message": "OK"}

# @router.get("/login")
# def login() -> list[dict]:
#     return ...
#
# @router.get("/logout")
# def logout() -> list[dict]:
#     return ...

