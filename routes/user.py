from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from crud.user import create_user, create_access_token_for_user
from database.db import get_db
from schemas.user import UserCreate, UserLogin

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/signup")
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db=db, user_data=user_data)
    if new_user:
        return {"msg": "User created successfully"}
    else:
        return {"msg": "User could not be created"}

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    access_token = create_access_token_for_user(db=db, user_data=user_data)
    if access_token:
        return {"msg": "Logged in successfully", "access_token": access_token, "token_type": "Bearer"}
    else:
        return {"msg": "Failed to login"}