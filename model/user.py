from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.orm import relationship

from database.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    todos = relationship("Todo", back_populates="user", cascade="all, delete")
