from fastapi.security import OAuth2PasswordBearer
from jwt import decode, PyJWTError
from sqlalchemy.orm import Session
from starlette import status
from models.user import User
from utils.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException
from datetime import timedelta
from schemas.user import UserCreate, UserLogin
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_user(db: Session, user_data: UserCreate):
    print(user_data)
    db_user = db.query(User).filter(user_data.email == User.email).first()
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

def get_current_user_id(db: Session, token: str = oauth2_scheme):
    try:
        payload = decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        user_email = payload.get("sub")
        if user_email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        user = db.query(User).filter(User.email == user_email).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return user.id
