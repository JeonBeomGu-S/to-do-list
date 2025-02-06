from datetime import datetime

from pydantic import BaseModel

class TodoCreate(BaseModel):
    user_id: int
    title: str
    description: str
    due_date: datetime
    priority: str

    class Config:
        orm_mode = True

class TodoUpdate(BaseModel):
    user_id: int
    title: str
    description: str
    due_date: datetime
    priority: str
    completed: bool

    class Config:
        orm_mode = True