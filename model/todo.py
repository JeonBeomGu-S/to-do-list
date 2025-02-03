from sqlalchemy import Column, String, Integer, DateTime, func, ForeignKey, Text, Boolean, CheckConstraint
from sqlalchemy.orm import relationship

from database.db import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(DateTime, nullable=True)
    priority = Column(String(10), CheckConstraint("priority IN ('low', 'medium', 'high')"), nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="todos")
    tags = relationship("TodoTag", back_populates="todo", cascade="all, delete")

