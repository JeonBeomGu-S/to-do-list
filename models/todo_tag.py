from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base


class TodoTag(Base):
    __tablename__ = "todo_tags"

    todo_id = Column(Integer, ForeignKey("todos.id", ondelete="CASCADE"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)

    todo = relationship("Todo", back_populates="tags")
    tag = relationship("Tag", back_populates="todos")