from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/signup")
def signup():
    return {"msg": "/users/signup"}

@router.post("/login")
def login():
    return {"msg": "/users/login"}

@router.post("/logout")
def login():
    return {"msg": "/users/logout"}

