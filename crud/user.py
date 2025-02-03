from sqlalchemy.orm import Session
from models.user import User
from utils.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException
from datetime import timedelta
from schemas.user import UserCreate, UserLogin
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_user(db: Session, user_data: UserCreate):
    print(user_data)
    db_user = db.query(User).filter(User.email == user_data.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="This email has already registered")

    hashed_password = hash_password(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, user_data: UserLogin):
    db_user = db.query(User).filter(User.email == user_data.email).first()
    if db_user is None or not verify_password(user_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="The email or password is incorrect")

    return db_user


def create_access_token_for_user(db: Session, user_data: UserLogin):
    user = authenticate_user(db, user_data)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return access_token
