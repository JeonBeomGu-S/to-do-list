from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.db import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    todos = relationship("TodoTag", back_populates="tag", cascade="all, delete")
